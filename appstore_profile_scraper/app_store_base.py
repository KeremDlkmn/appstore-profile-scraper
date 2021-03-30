import logging
import random
import re
import requests
import sys
import time
from datetime import datetime
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Base():
    _scheme = "https"

    _landing_host = ""
    _request_host = ""

    _landing_path = ""
    _request_path = ""

    _user_agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36'"
    ]

    def __init__(
        self,
        country,
        app_name,
        app_id=None
    ):
        self._base_landing_url = f"{self._scheme}://{self._landing_host}"
        self._base_request_url = f"{self._scheme}://{self._request_host}"

        self.country = str(country).lower()
        self.app_name = re.sub(r"[\W_]+", "-", str(app_name).lower())
        if app_id is None:
            app_id = self.search_id()
        self.app_id = int(app_id)

        self.url = self._landing_url()

        self._request_url = self._request_url()

        self._request_headers = {
            "Accept": "application/json",
            "Authorization": self._token(),
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": self._base_landing_url,
            "Referer": self.url,
            "User-Agent": random.choice(self._user_agents),
        }

        self._request_params = {}
        self._response = requests.Response()
        self._profile_data = {}

    def __repr__(self):
        return "{}(country='{}', app_name='{}', app_id={})".format(
            self.__class__.__name__,
            self.country,
            self.app_name,
            self.app_id,
        )

    def _landing_url(self):
        landing_url = f"{self._base_landing_url}/{self._landing_path}"
        return landing_url.format(
            country=self.country, app_name=self.app_name, app_id=self.app_id
        )

    def _request_url(self):
        request_url = f"{self._base_request_url}/{self._request_path}"
        return request_url.format(country=self.country, app_id=self.app_id)

    def _get(
        self,
        url,
        headers=None,
        params=None,
        total=3,
        backoff_factor=3,
        status_forcelist=[404, 429],
    ) -> requests.Response:
        retries = Retry(
            total=total,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        with requests.Session() as s:
            s.mount(self._base_request_url, HTTPAdapter(max_retries=retries))
            self._response = s.get(url, headers=headers, params=params)

    def _token(self):
        self._get(self.url)
        tags = self._response.text.splitlines()
        for tag in tags:
            if re.match(r"<meta.+web-experience-app/config/environment", tag):
                token = re.search(r"token%22%3A%22(.+?)%22", tag).group(1)
                return f"bearer {token}"

    def _parse_data(self):
        response = self._response.json()

        for data in response['data']:
            if ('subtitle' in data['attributes']['platformAttributes']['ios'].keys()):
                self._profile_data = {
                    "id": data['id'],
                    "app_name": data['attributes']['name'],
                    "app_develop_name": data['attributes']['artistName'],
                    "app_url": data['attributes']['url'],
                    "app_icon": data['attributes']['platformAttributes']['ios']['artwork']['url'].replace("{w}x{h}{c}.{f}", "230x0w.webp"),
                    "app_subtitle": data['attributes']['platformAttributes']['ios']['subtitle'],
                    "app_bundleID": data['attributes']['platformAttributes']['ios']['bundleId'],
                    "app_raiting": data['attributes']['userRating'],
                }
            else:
                self._profile_data = {
                    "id": data['id'],
                    "app_name": data['attributes']['name'],
                    "app_develop_name": data['attributes']['artistName'],
                    "app_url": data['attributes']['url'],
                    "app_icon": data['attributes']['platformAttributes']['ios']['artwork']['url'].replace("{w}x{h}{c}.{f}", "230x0w.webp"),
                    "app_subtitle": "NONE",
                    "app_bundleID": data['attributes']['platformAttributes']['ios']['bundleId'],
                    "app_raiting": data['attributes']['userRating'],
                }

        return self._profile_data

    def search_id(self):
        search_url = "https://www.google.com/search"
        self._get(search_url, params={"q": f"app store {self.app_name}"})
        pattern = fr"{self._base_landing_url}/[a-z]{{2}}/.+?/id([0-9]+)"
        app_id = re.search(pattern, self._response.text).group(1)
        return app_id

    def profile_info(self):
        self._get(
            self._request_url,
            headers=self._request_headers,
            params=self._request_params
        )
        return self._parse_data()

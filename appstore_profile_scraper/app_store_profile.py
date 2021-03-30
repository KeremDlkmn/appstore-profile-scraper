from appstore_profile_scraper.app_store_base import Base


class AppStoreProfile(Base):
    _landing_host = "apps.apple.com"
    _request_host = "amp-api.apps.apple.com"

    _landing_path = "{country}/app/{app_name}/id{app_id}"
    _request_path = "v1/catalog/{country}/apps/{app_id}"

    def __init__(
        self,
        country,
        app_name,
        app_id=None,
    ):
        super().__init__(
            country=country,
            app_name=app_name,
            app_id=app_id
        )

        # override
        self._request_params = {
            "l": "en-GB",
            "ids":self.app_id,
            "platform": "web",
            "additionalPlatforms": "appletv,ipad,iphone,mac",
        }

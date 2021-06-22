[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
[![Build: Passing](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/KeremDlkmn/appstore-profile-scraper)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/KeremDlkmn/appstore-profile-scraper)
[![pypi: v0.0.10](https://img.shields.io/badge/pypi-v0.0.10-yellow.svg)](https://pypi.org/project/appstore-profile-scraper/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/appstore-profile-scraper)

![appstore-profile-scrapper](https://user-images.githubusercontent.com/25768758/122870011-cb272600-d335-11eb-8bd6-ddd40bdedd5d.png)

# Apple App Store Profile Scrapper
With the Apple App Store Profile Scrapper, you can access the profile information of the applications published in the app store.

# Installation
The easiest way to install *appstore-profile-scraper* is to download it from [PyPI](https://pypi.org/project/appstore-profile-scraper/)
```python
pip install appstore-profile-scraper
```

Scrape profile for an app:
```python
from appstore_profile_scraper import AppStoreProfile

apps = AppStoreProfile(
    country="tr", 
    app_name="instagram"
)

if __name__ == '__main__':
    print(apps.profile_info())
```

Scrape profile for an app:
> *NOTE: If the application name contains characters in the format of utf-8, the following code block can be used.*
```python
from appstore_profile_scraper import AppStoreProfile

apps = AppStoreProfile(
    country="tr", 
    app_name="instagram".encode('utf-8').decode('latin-1')
)

if __name__ == '__main__':
    print(apps.profile_info())
```

# Details
* country(required): two-letter country code of [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard
* app_name(required): name of an iOS application to fetch profile information for.

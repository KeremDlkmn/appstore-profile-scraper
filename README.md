[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
[![pypi: v0.0.10](https://img.shields.io/badge/pypi-v0.0.10-yellow.svg)](https://pypi.org/project/appstore-profile-scraper/)
[![Build: Passing](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/KeremDlkmn/appstore-profile-scraper)
![PyPI - Downloads](https://img.shields.io/pypi/dm/appstore-profile-scraper)

![appstore-profile-scraper](https://socialify.git.ci/KeremDlkmn/appstore-profile-scraper/image?description=1&descriptionEditable=With%20Apple%20App%20Store%20Profile%20Scraper%2C%20it%20allows%20you%20to%20access%20profile%20information%20of%20applications%20published%20in%20the%20app%20store.&font=Raleway&pattern=Brick%20Wall&theme=Light)

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
* app_name(required): name of an iOS application to fetch profile information for

import importlib
import json
import requests
import yaml

from bs4 import BeautifulSoup

from api.common import config
from api.common.company import Company
from api.crawlers.crawer import Crawler


def process_data():
    conf = config.get_config()
    for site in conf["sites"]:
        print(f"Crawling {site['name']}...")
        crawler_module = importlib.import_module(f"api.crawlers.{site['slug']}")
        crawler: Crawler = getattr(crawler_module, site['slug'].title())()
        companies = crawler.get_companies()
        print("\n".join(f"  {c.name:>30}: {c.logo_url}" for c in companies))
        save_companies(site['slug'], companies)


def save_companies(site_slug: str, companies: list[Company]):
    raw_data = [{"name": c.name, "logo_url": c.logo_url} for c in companies]
    open(f"data/{site_slug}.json", "w").write(json.dumps(raw_data))


process_data()

# # url = "https://scale.com"
# # html = requests.get(url).content
# # soup = BeautifulSoup(html, 'html.parser')
# # els = soup.select("section.text-white:nth-child(1) li img")
# # for el in els:
# #     slug = el["alt"]
# #     src = el["src"]
# #     imgurl = f"{url}{el['src']}"


# # https://scale.com/

# # /_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fmicrosoft.svg&amp;w=256&amp;q=100
# # /_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fmicrosoft.svg&amp;w=128&amp;q=100 1x
# # /_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fmicrosoft.svg&amp;w=256&amp;q=100 2x
# # https://scale.com/_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fmicrosoft.svg&amp;w=256&amp;q=100
# # https://scale.com/static/images/logos/customers/microsoft.svg&amp;w=256&amp;q=100
# # https://scale.com/_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fmicrosoft.svg&w=256&q=100


# import requests
# from bs4 import BeautifulSoup

# _base_url = "https://webflow.com"

# html = requests.get(_base_url).content
# soup = BeautifulSoup(html, 'html.parser')
# soup.select("section.cc-enterprise .intro-logos_wrapper")

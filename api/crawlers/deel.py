import re
import requests

from bs4 import BeautifulSoup

from api.crawlers import crawer
from api.common.company import Company


class Deel(crawer.Crawler):

    _base_url = "https://www.deel.com/"

    def get_companies(self) -> list[dict]:
        html = requests.get(self._base_url).content
        soup = BeautifulSoup(html, 'html.parser')
        els = soup.select(".logo-scroll-inner .scroll-looper-sec .single-image img")
        companies = []
        for el in els:
            name = el["alt"].lower()
            finds = ["[._-]?white[._-]?", "[._-]?logo[._-]?", " 1", "[._-]?20\d\d[._-]?"]
            for f in finds:
                name = re.sub(f, "", name)
            name = name.replace("_", " ").title()
            companies.append(Company(name=name, logo_url=el["src"]))
        return companies

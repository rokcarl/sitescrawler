import requests

from bs4 import BeautifulSoup

from api.crawlers import crawer
from api.common.company import Company


class Webflow(crawer.Crawler):

    _base_url = "https://webflow.com"

    def get_companies(self) -> list[dict]:
        html = requests.get(self._base_url).content
        soup = BeautifulSoup(html, 'html.parser')
        els = soup.select("section.cc-enterprise .intro-logos_wrapper .intro-logos_logo")
        companies = []
        for el in els:
            name = el["alt"]
            if not name:
                continue
            companies.append(Company(name=name, logo_url=el["src"]))
        # the elements are duplicated for scrolling, so take only unique ones
        companies = {c.name: c for c in companies}.values()
        return companies

import requests

from bs4 import BeautifulSoup

from api.crawlers import crawer
from api.common.company import Company


class Scale(crawer.Crawler):

    _base_url = "https://scale.com/"

    def get_companies(self) -> list[dict]:
        html = requests.get(self._base_url).content
        soup = BeautifulSoup(html, 'html.parser')
        els = soup.select("section.text-white:nth-child(1) li img")
        companies = []
        for el in els:
            company = Company(name=el["alt"].title(), logo_url=f"{self._base_url}{el['src']}")
            companies.append(company)
        return companies

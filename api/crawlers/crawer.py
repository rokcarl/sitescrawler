from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from api.common.company import Company

class Crawler(ABC):
    @abstractmethod
    def get_companies(self) -> list[Company]:
        pass

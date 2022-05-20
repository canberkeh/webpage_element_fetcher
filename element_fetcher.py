from bs4 import BeautifulSoup
from get_request import GetRequest

class ElementFetcher(GetRequest):
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.soup = BeautifulSoup(self.execute_request(), "html.parser")

    def fetch_links(self) -> dict:
        links = {iterable: self.soup.find_all("a")[iterable].get("href") for iterable in range(len(self.soup.find_all("a")))}
        return links

    def fetch_images(self) -> dict:
        images = {iterable: self.soup.find_all("img")[iterable].get("src") for iterable in range(len(self.soup.find_all("img")))}
        return images

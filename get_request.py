import requests
from generate_headers import headers


class GetRequest():
    def __init__(self, url: str) -> None:
        if "https://" in url or "http://" in url:
            self.url = url
        else:
            self.url = "https://" + url

    def execute_request(self) -> str:
        response = requests.get(url=self.url, headers=headers())
        return response.text

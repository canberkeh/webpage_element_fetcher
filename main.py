from pprint import pprint
from element_fetcher import ElementFetcher

url = "https://pypi.org" # set url here
element_fetcher = ElementFetcher(url=url)
print("Links")
pprint(element_fetcher.fetch_links())
print("\n")
print("Images")
pprint(element_fetcher.fetch_images())

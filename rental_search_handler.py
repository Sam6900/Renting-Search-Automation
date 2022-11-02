import requests
from bs4 import BeautifulSoup

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


class RentalSearchHandler:
    def __init__(self, search_url):
        response = requests.get(search_url, headers=req_headers)
        zillow_data = response.text
        self.soup = BeautifulSoup(zillow_data, "html.parser")

    def get_addresses(self):
        addresses = [addr.get_text() for addr in self.soup.select("a address")]
        return addresses

    def get_prices(self):
        prices = []
        for price in self.soup.select(".hRqIYX span"):
            price = price.get_text()
            if "/" in price:
                price = price.split("/")[0]
            elif "+" in price:
                price = price.split("+")[0]
            prices.append(price)
        return prices

    def get_place_links(self):
        links = []
        for link_tag in self.soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0"):
            link = link_tag.get("href")
            if not link.startswith("https"):
                link = "https://www.zillow.com" + link
            links.append(link)
        return links

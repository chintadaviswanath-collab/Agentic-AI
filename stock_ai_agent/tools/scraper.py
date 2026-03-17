import requests
from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self, url):
        self.url = url

    def fetch_page(self):

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(self.url, headers=headers)

        if response.status_code != 200:
            print("Failed to fetch page")
            return None

        return response.text


    def parse_html(self, html):

        soup = BeautifulSoup(html, "html.parser")

        return soup


    def get_text(self, soup, tag):

        elements = soup.find_all(tag)

        return [e.text.strip() for e in elements]

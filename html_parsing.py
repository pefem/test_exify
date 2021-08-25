import requests
from bs4 import BeautifulSoup


def parse_product_name(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    outter_wrap = soup.select_one(".caption")

    product_name = outter_wrap.select("h4")[1].get_text()
    return product_name


def parse_product_description(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    outter_wrap = soup.select_one(".caption")

    product_description = outter_wrap.select_one(".description").get_text()
    return product_description


def parse_product_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    outter_wrap = soup.select_one(".caption")

    product_price = outter_wrap.select("h4")[0].get_text()
    return product_price
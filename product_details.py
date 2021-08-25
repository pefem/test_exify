import requests
from bs4 import BeautifulSoup
import sqlite3
import product_links
import json
from pathlib import Path


class ProductDetails:

    def __init__(self, start) -> None:
        self.products = product_links.Products(start)
        self.products.get_product_links()
    

    def get_links_from_db(self):
        product_links = []

        with sqlite3.connect("db.exify") as conn:
            command = "SELECT * FROM tb_productlinks"
            cursor = conn.execute(command)
            for row in cursor:
                product_links.append(row[0])
        
        return product_links


    def process_links(self, links):
        products = []

        for link in links:
            response = requests.get(link, self.products.headers)

            page_soup = BeautifulSoup(response.text, "html.parser")
            outter_wrap = page_soup.select_one(".caption")

            product_name = outter_wrap.select("h4")[1].get_text()
            product_description = outter_wrap.select_one(".description").get_text()
            product_price = outter_wrap.select("h4")[0].get_text()

            item = {
                "name": product_name,
                "description": product_description,
                "price": product_price
            }

            products.append(item)
        
        return products


    def write_to_file(self, products):

        data = json.dumps(products)
        Path("products.json").write_text(data)




if __name__ == "__manin__":
    details = ProductDetails("https://webscraper.io/test-sites/e-commerce/allinone")
    a = details.get_links_from_db()
    b = details.process_links(a)
    details.write_to_file(b)
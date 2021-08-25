import requests
from bs4 import BeautifulSoup
import sqlite3


class Products:

    def __init__(self, start_url) -> None:
        self.start_url = start_url
        self.base_url = "https://webscraper.io"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    

    def get_product_links(self):
        response = requests.get(self.start_url, headers=self.headers)
        page_soup = BeautifulSoup(response.text, "html.parser")

        outter_wrap = page_soup.select(".col-sm-4.col-lg-4.col-md-4")
        for tag in outter_wrap:
            link = tag.select("h4")[1].a["href"]
            combined_link = f"{self.base_url}{link}"

            product = {"link": combined_link}
            
            with sqlite3.connect("db.exify") as conn:
                command = "INSERT INTO tb_productlinks VALUES(?)"
                conn.execute(command, tuple(product.values()))

                conn.commit()
        
        print("product links added to database")
    
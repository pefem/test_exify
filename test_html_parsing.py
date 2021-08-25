import unittest
import html_parsing

#url = "https://webscraper.io/test-sites/e-commerce/allinone/product/626"

class TestParsing(unittest.TestCase):
    
    def test_parse_product_name(self):
        result = html_parsing.parse_product_name("enter url")
        self.assertIsNotNone(result)

    def test_parse_product_description(self):
        result = html_parsing.parse_product_description("enter url")
        self.assertIsNotNone(result)

    def test_parse_product_price(self):
        result = html_parsing.parse_product_price("enter url")
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
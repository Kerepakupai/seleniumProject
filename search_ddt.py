import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack
import csv


def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows


@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        options = Options()
        # options.headless = True
        cls.driver = webdriver.Chrome(service=service, options=options)
        driver = cls.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.click()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')

        expected_count = int(expected_count)
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element(By.CLASS_NAME, "note-msg")
            self.assertEqual("    Your search returns no results.        ", message)

        print(f"Found {len(products)} products")

        # for product in products:
            # print(product.text)

        # self.assertEqual(expected_count, len(products))

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Typos(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        options = Options()
        # options.headless = True
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get("https://mercadolibre.com/")
        cls.driver.maximize_window()

    def test_search_ps5(self):
        driver = self.driver
        driver.find_element(By.ID, "CL").click()
        sleep(3)

        # Search
        search_field = driver.find_element(By.NAME, "as_word")
        search_field.click()
        search_field.clear()
        search_field.send_keys("ps5")
        search_field.submit()
        sleep(3)

        # Condition filter
        condition = driver.find_element(By.PARTIAL_LINK_TEXT, "Nuevo")
        condition.click()
        sleep(3)

        # Location
        # location = driver.find_element(By.XPATH, "'/html/body/main/div/div[2]/aside/section[2]/div[6]/ul/li[1]/a'")
        # location.click()
        # sleep(3)

        # Sort
        sort = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/div[1]/div/div/div/div[2]/div/button')
        sort.click()
        sleep(3)
        price_asc = driver.find_element(By.XPATH, '//*[@id="andes-dropdown-más-relevantes-list-option-price_asc"]')
        price_asc.click()
        sleep(3)

        # Articles
        products_element = driver.find_elements(
            By.XPATH,
            '//div[@class="ui-search-item__group ui-search-item__group--title"]/a/h2')
        products = list(map(lambda product: product.text, products_element))
        print(products)

        # Prices
        # prices = driver.find_elements(By.XPATH, '//span[@class="ui-search-item__title"')
        # print(prices)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


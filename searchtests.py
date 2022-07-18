import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.implicitly_wait(15)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(by=By.NAME, value="q")
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(by=By.NAME, value="q")

        search_field.send_keys(("salt shaker"))
        search_field.submit()

        products = driver.find_elements(
            by=By.XPATH,
            value='//div[@class="category-products"]/ul/li/a[@class="product-image"]')
        self.assertEqual(1, len(products))

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

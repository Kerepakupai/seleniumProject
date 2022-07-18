import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePageTests(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_field = self.driver.find_element(by=By.ID, value="search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(by=By.NAME, value="q")

    def test_search_text_field_by_class(self):
        search_field = self.driver.find_element(by=By.CLASS_NAME, value="input-text")

    def test_search_button_enable(self):
        search_field = self.driver.find_element(by=By.CLASS_NAME, value="button")

    def test_count_of_promo_banners_images(self):
        banners_list = self.driver.find_element(by=By.CLASS_NAME, value="promos")
        banners = banners_list.find_elements(by=By.TAG_NAME, value="img")
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(by=By.XPATH, value='//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element(by=By.CSS_SELECTOR, value="div.header-minicart span.icon")

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

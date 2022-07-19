import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class CompareProducts(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.implicitly_wait(15)

    def test_compare_products_remove_alert(self):
        driver = self.driver
        search_field = driver.find_element(by=By.ID, value="search")
        search_field.clear()
        search_field.send_keys("tee")
        search_field.submit()

        driver.find_element(by=By.CLASS_NAME, value="link-compare").click()

        driver.find_element(by=By.LINK_TEXT, value="Clear All").click()
        alert = driver.switch_to.alert
        alert_text = alert.text
        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)
        alert.accept()

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

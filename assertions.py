import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.implicitly_wait(15)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as ne:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)

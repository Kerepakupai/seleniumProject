import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from google_page import GooglePage


class Typos(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="../chromedriver.exe")
        options = Options()
        options.headless = True
        cls.driver = webdriver.Chrome(service=service, options=options)

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search("Platzi")

        self.assertEqual("Platzi", google.keyword)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


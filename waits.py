import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class CompareProducts(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        options = Options()
        # options.headless = True
        cls.driver = webdriver.Chrome(service=service, options=options)
        driver = cls.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.implicitly_wait(15)
        driver.find_element(by=By.LINK_TEXT, value="Disappearing Elements").click()

    def test_name_elements(self):
        driver = self.driver
        options = []
        menu = 5
        tries = 1

        while len(options) < menu:
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element(by=By.XPATH, value=f"//ul/li[{i+1}]/a")
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option {i+1} not found")
                    tries += 1
                    driver.refresh()

            print(f"Finished in {tries} tries")

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

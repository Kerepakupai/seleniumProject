import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class Typos(unittest.TestCase):

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
        driver.find_element(By.LINK_TEXT, "Typos").click()

    def test_find_typo(self):
        driver = self.driver
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            print("Inside while loops")
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh()
            tries += 1
        print(f"Tries {tries}")

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

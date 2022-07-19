import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):

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
        driver.find_element(By.LINK_TEXT, "Dynamic Controls").click()

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")
        checkbox.click()

        remove_add_button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example > button")
        remove_add_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_button.click()

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, "#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))

        text_area = driver.find_element(By.CSS_SELECTOR, "#input-example > input[type=text]")
        text_area.send_keys("Kerepakupai")
        enable_disable_button.click()

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AddRemoveElements(unittest.TestCase):

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
        driver.find_element(by=By.LINK_TEXT, value="Add/Remove Elements").click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input("How many elements will you add?: "))
        elements_removed = int(input("How many elements will you remove?: "))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(by=By.XPATH, value='//div[@class="example"]/button')

        sleep(3)
        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                remove_button = driver.find_element(by=By.XPATH, value='//div[@id="elements"]/button[1]')
                remove_button.click()
            except:
                print("You're trying to remove more elements than the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print(f"There are 0 elements on screen")

        sleep(3)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterNewUser(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        service = Service(executable_path="./chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.implicitly_wait(15)

    def test_new_user(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value='//div[@class="account-cart-wrapper"]/a[1]').click()
        driver.find_element(by=By.LINK_TEXT, value="Log In").click()

        create_account_button = driver.find_element(
            by=By.XPATH,
            value='//a[@title="Create an Account" and @class="button"]')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(by=By.ID, value="firstname")
        middle_name = driver.find_element(by=By.ID, value="middlename")
        last_name = driver.find_element(by=By.ID, value="lastname")
        email_address = driver.find_element(by=By.ID, value="email_address")
        password = driver.find_element(by=By.ID, value="password")
        pass_confirmation = driver.find_element(by=By.ID, value="confirmation")
        newsletter = driver.find_element(by=By.ID, value="is_subscribed")
        submit_button = driver.find_element(by=By.XPATH, value='//button[@class="button" and @title="Register"]')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and pass_confirmation.is_enabled()
                        and newsletter.is_enabled()
                        and submit_button.is_enabled())

        first_name.send_keys("Test")
        middle_name.send_keys("Test")
        last_name.send_keys("Test")
        email_address.send_keys("test@test.com")
        password.send_keys("password")
        pass_confirmation.send_keys("password")
        newsletter.click()
        driver.implicitly_wait(5)
        submit_button.click()

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

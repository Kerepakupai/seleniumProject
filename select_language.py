import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(self.driver.find_element(by=By.ID, value="select-language"))

        self.assertEqual(len(exp_options), len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)
        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text("German")
        self.assertTrue("store=german" in self.driver.current_url)

        select_language = Select(self.driver.find_element(by=By.ID, value="select-language"))
        select_language.select_by_index(0)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

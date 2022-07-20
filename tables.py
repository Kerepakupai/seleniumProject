import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class Tables(unittest.TestCase):

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
        driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

    def test_sort_tables(self):
        driver = self.driver
        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)

            for j in range(4):
                row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{j+1}]')
                table_data[i].append(row_data.text)

        print(table_data)

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.implicitly_wait(15)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

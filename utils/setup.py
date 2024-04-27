from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSetup:

    @classmethod
    def create_driver(cls):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver

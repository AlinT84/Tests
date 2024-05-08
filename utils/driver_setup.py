from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverSetup:

    def __init__(self):
        self.driver = None

    @classmethod
    def create_driver(cls):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)
        driver.set_window_size(1920, 1080)
        driver.maximize_window()
        return driver

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from sesiunea_11_12.tests.utils.constants import URL

URL = URL
# COOKIES_BUTTON = (By.XPATH, '//button[contains(text(),"Accept toate")]')
# LOGIN_X_BUTTON = (By.XPATH, '//button/i[@class="em em-close"]')


def handle_cookies_acceptance(self):
    try:
        cookies_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COOKIES_BUTTON)
        )
        cookies_button.click()
        print("Cookies acceptance dialog handled.")
    except Exception as e:
        print("Cookies acceptance dialog not found or already accepted.")


def handle_login_dialog(self):
    try:
        login_x_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_X_BUTTON)
        )
        login_x_button.click()
        print("Login dialog handled.")
    except Exception as e:
        print("Login dialog not found or already closed.")


class AlertHandlers(unittest.TestCase):
    global URL
    driver = None
    BUTON_JS_ALERT = (By.XPATH, '//button[@onclick="jsAlert()"]')
    BUTON_JS_CONFIRM = (By.XPATH, '//button[@onclick="jsConfirm()"]')
    BUTON_JS_PROMPT = (By.XPATH, '//button[@onclick="jsPrompt()"]')

    MESAJE = (By.ID, "result")

    # suprascriem metoda de setUp care va rula inainte de orice test
    def setUp(self) -> None:
        # self.service_chrome = Service(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=self.service_chrome)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    # suprascriem metoda de tearDown care va rula dupa orice test
    def tearDown(self) -> None:
        self.driver.quit()

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    # @unittest.skip
    def test_accept_simple_alert(self):
        # time.sleep(3)
        self.click(self.BUTON_JS_ALERT)
        # time.sleep(3)
        # pentru interactionarea cu alerte avem functia de "switch to"
        # declararea unei variabile "alerta" pentru a putea interactiona cu ea
        alerta = self.driver.switch_to.alert

        # pentru a inchide alerta aceasta trebuie acceptata
        alerta.accept()
        # time.sleep(3)
        expected_text = "You successfully clicked an alert"
        actual_text = self.get_text(self.MESAJE)
        self.assertEqual(expected_text, actual_text, f"ERROR WRONG MESSAGE")

    # @unittest.skip
    def test_accept_confirm_alert(self):
        # time.sleep(3)
        self.click(self.BUTON_JS_CONFIRM)
        # time.sleep(3)
        # pentru interactionarea cu alerte avem functia de "switch to"
        # declararea unei variabile "alerta" pentru a putea interactiona cu ea
        alerta = self.driver.switch_to.alert

        # pentru a inchide alerta aceasta trebuie acceptata
        alerta.accept()
        # time.sleep(3)
        expected_text = "You clicked: Ok"
        actual_text = self.get_text(self.MESAJE)
        self.assertEqual(expected_text, actual_text, f"ERROR WRONG MESSAGE")

    # @unittest.skip
    def test_cancel_confirm_alert(self):
        # time.sleep(3)
        self.click(self.BUTON_JS_CONFIRM)
        # time.sleep(3)
        # pentru interactionarea cu alerte avem functia de "switch to"
        # declararea unei variabile "alerta" pentru a putea interactiona cu ea
        alerta = self.driver.switch_to.alert

        # pentru a inchide alerta aceasta trebuie acceptata
        alerta.dismiss()
        # time.sleep(3)
        expected_text = "You clicked: Cancel"
        actual_text = self.get_text(self.MESAJE)
        self.assertEqual(expected_text, actual_text, f"ERROR WRONG MESSAGE")

    # @unittest.skip
    def test_accept_empty_prompt_alert(self):
        # time.sleep(3)
        self.click(self.BUTON_JS_PROMPT)
        # time.sleep(3)
        # pentru interactionarea cu alerte avem functia de "switch to"
        # declararea unei variabile "alerta" pentru a putea interactiona cu ea
        alerta = self.driver.switch_to.alert

        # pentru a inchide alerta aceasta trebuie acceptata
        alerta.accept()
        # time.sleep(2)
        expected_text = "You entered:"
        actual_text = self.get_text(self.MESAJE)
        self.assertEqual(expected_text, actual_text, f"ERROR WRONG MESSAGE")

    def test_accept_fill_prompt_alert(self):
        # time.sleep(3)
        self.click(self.BUTON_JS_PROMPT)
        # time.sleep(3)
        # pentru interactionarea cu alerte avem functia de "switch to"
        # declararea unei variabile "alerta" pentru a putea interactiona cu ea
        alerta = self.driver.switch_to.alert

        # time.sleep(3)
        input_text = "TEST ALERTA"

        alerta.send_keys(input_text)
        # time.sleep(2)
        alerta.accept()
        # time.sleep(2)
        expected_text = "You entered: " + input_text
        actual_text = self.get_text(self.MESAJE)
        self.assertEqual(expected_text, actual_text)

    def test_cancel_prompt_alert(self):
        # time.sleep(3)
        self.click(self.BUTON_JS_PROMPT)
        # time.sleep(3)
        # pentru interactionarea cu alerte avem functia de "switch to"
        # declararea unei variabile "alerta" pentru a putea interactiona cu ea
        alerta = self.driver.switch_to.alert

        # pentru a inchide alerta aceasta trebuie acceptata
        alerta.dismiss()
        # time.sleep(2)
        expected_text = "You entered: null"
        actual_text = self.get_text(self.MESAJE)
        self.assertEqual(expected_text, actual_text, f"ERROR WRONG MESSAGE")

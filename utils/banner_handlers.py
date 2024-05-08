from ..utils.methods import wait_and_click_element
from ..utils.constants import COOKIES_BUTTON, LOGIN_X_BUTTON


class BannerHandler:
    def __init__(self, driver):
        self.driver = None

    def accept_cookies(self):
        try:
            wait_and_click_element(self.driver, COOKIES_BUTTON)
            print("Cookies dialog handled.")
        except Exception:
            print("Cookies dialog not found or already closed.")

    def close_login_dialog(self):
        try:
            wait_and_click_element(self.driver, LOGIN_X_BUTTON)
            print("Login dialog handled.")
        except Exception:
            print("Login dialog not found or already closed.")

def handle_dialogs(driver):
    """Call this method after any action that may cause the page to refresh."""
    handler = BannerHandler(driver)
    handler.accept_cookies()
    handler.close_login_dialog()

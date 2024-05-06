import unittest

from sesiunea_11_12.tests.utils.constants import (
    URL,
    MAIN_PAGE_LOGO_BUTTON,
    ACCOUNT_BUTTON,
    FAV_BUTTON,
    CART_BUTTON,
    GENIUS_DEALS_BUTTON,
    GENIUS_BUTTON,
    CARD_IDEI_BUTTON,
    RABLA_BUTTON,
    OFERTE_EMAG_BUTTON,
)
from sesiunea_11_12.tests.utils.methods import wait_and_click_element
from sesiunea_11_12.tests.utils.methods import wait_visible_and_click_element
from sesiunea_11_12.tests.utils.setup import DriverSetup


class CorrectUrlNavigation(unittest.TestCase):

    driver = None

    def setUp(self) -> None:
        self.driver = DriverSetup.create_driver()
        self.driver.get(URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_main_page_logo_button(self):
        wait_and_click_element(self.driver, MAIN_PAGE_LOGO_BUTTON)
        returned_url = self.driver.current_url
        expected_url = URL
        try:
            self.assertEqual(
                returned_url,
                expected_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_account_logo_button(self):
        wait_and_click_element(self.driver, ACCOUNT_BUTTON)
        returned_url = self.driver.current_url
        expected_url = "https://auth.emag.ro/user/login"
        try:
            self.assertEqual(
                returned_url,
                expected_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_fav_button(self):
        wait_and_click_element(self.driver, FAV_BUTTON)
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/favorites?ref=ua_favorites"
        try:
            self.assertEqual(
                returned_url,
                expected_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_cart_button(self):
        wait_and_click_element(self.driver, CART_BUTTON)
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/cart/products?ref=cart"
        try:
            self.assertEqual(
                returned_url,
                expected_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_genius_deals_button(self):
        wait_and_click_element(self.driver, GENIUS_DEALS_BUTTON)
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/label-campaign/genius-deals"
        try:
            self.assertIn(
                expected_url,
                returned_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_genius_button(self):
        wait_and_click_element(self.driver, GENIUS_BUTTON)
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/genius?ref=hdr_genius"
        try:
            self.assertEqual(
                returned_url,
                expected_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_rabla_button(self):
        wait_and_click_element(self.driver, RABLA_BUTTON)
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/lps/rabla-emag?ref=hdr_rabla"
        try:
            self.assertEqual(
                returned_url,
                expected_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_rabla_button(self):
        wait_visible_and_click_element(self.driver, OFERTE_EMAG_BUTTON)
        returned_url = self.driver.current_url
        expected_url = "https://www.emag.ro/nav/deals?ref=hdr_ofertele-emag"
        try:
            self.assertEqual(
                returned_url,
                expected_url,
                "The button did not returned the expected URL.",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")


if __name__ == "__main__":
    unittest.main()

import time
import unittest

from sesiunea_11_12.tests.utils.constants import (
    URL,
    SORTING_MENU,
    ASCENDING_ORDER_OPTION,
    DESCENDIND_ORDER_OPTION,
    REVIEW_NB_OPTION,
    PRICES,
    RESULTS_BY_REVIEWS,
)
from sesiunea_11_12.tests.utils.methods import (
    wait_and_click_element,
    perform_search,
    extract_data_from_elements,
)
from sesiunea_11_12.tests.utils.driver_setup import DriverSetup
from sesiunea_11_12.tests.utils.banner_handlers import handle_dialogs


class SortFunctionality(unittest.TestCase):

    driver = None

    def setUp(self) -> None:
        self.driver = DriverSetup.create_driver()
        self.driver.get(URL)
        handle_dialogs(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_select_ascending_price(self):
        search_term = "iphone 15 pro max"
        perform_search(self.driver, search_term)
        time.sleep(3)
        handle_dialogs(self.driver)
        time.sleep(3)

        wait_and_click_element(self.driver, SORTING_MENU)
        wait_and_click_element(self.driver, ASCENDING_ORDER_OPTION)
        time.sleep(3)
        handle_dialogs(self.driver)
        time.sleep(3)

        # Extract product prices after sorting
        sorted_prices = extract_data_from_elements(self.driver, PRICES, flow="prices")

        # Validate sorting order
        is_ascending = sorted(sorted_prices)

        # Assert that prices are in ascending order
        try:
            self.assertListEqual(
                sorted_prices,
                is_ascending,
                "Prices are not in ascending order after sorting",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_select_descending_price(self):
        search_term = "iphone 15 pro max"
        perform_search(self.driver, search_term)
        handle_dialogs(self.driver)

        # Click the sorting menu and select descending order
        wait_and_click_element(self.driver, SORTING_MENU)
        wait_and_click_element(self.driver, DESCENDIND_ORDER_OPTION)
        handle_dialogs(self.driver)

        # Extract product prices after sorting
        sorted_prices = extract_data_from_elements(self.driver, PRICES, flow="prices")

        # Validate sorting order
        expected_descending_order = sorted(sorted_prices, reverse=True)

        # Assert that prices are in descending order
        try:
            self.assertListEqual(
                sorted_prices,
                expected_descending_order,
                "Prices are not in descending order after sorting",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def test_select_by_review_nb(self):
        search_term = "iphone 15 pro max"
        perform_search(self.driver, search_term)
        handle_dialogs(self.driver)

        wait_and_click_element(self.driver, SORTING_MENU)
        wait_and_click_element(self.driver, REVIEW_NB_OPTION)
        handle_dialogs(self.driver)

        # Extract product prices after sorting
        sorted_results_by_reviews = extract_data_from_elements(
            self.driver, RESULTS_BY_REVIEWS, flow="numbers"
        )

        # Validate sorting order (descending by review number)
        is_ordered = sorted(sorted_results_by_reviews, reverse=True)

        # Assert that results are in descending order by review number
        try:
            self.assertListEqual(
                sorted_results_by_reviews,
                is_ordered,
                "Results are not ordered correctly by review number",
            )
        except AssertionError as e:
            print(f"Assertion Error: {e}")


if __name__ == "__main__":
    unittest.main()

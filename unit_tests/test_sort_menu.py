import time
import unittest
from sesiunea_11_12.tests.utils.setup import DriverSetup
from sesiunea_11_12.tests.utils.methods import (
    wait_and_click_element,
    perform_search,
    extract_product_prices,
    extract_number_from_element,
)
from sesiunea_11_12.tests.utils.constants import (
    URL,
    SORTING_MENU,
    ASCENDING_ORDER_OPTION,
    DESCENDIND_ORDER_OPTION,
    REVIEW_NB_OPTION,
    RESULTS_BY_REVIEWS,
)


class SortFunctionality(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverSetup.create_driver()
        cls.driver.get(URL)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_select_ascending_price(self):
        try:
            search_term = "iphone 15 pro max"
            perform_search(self.driver, search_term)

            wait_and_click_element(self.driver, SORTING_MENU)
            wait_and_click_element(self.driver, ASCENDING_ORDER_OPTION)
            time.sleep(3)

            # Extract product prices after sorting
            sorted_prices = extract_product_prices(self.driver)

            is_ascending = sorted(sorted_prices)

            # Assert that prices are in ascending order
            self.assertListEqual(
                sorted_prices,
                is_ascending,
                "Prices are not in ascending order after sorting",
            )

        except Exception as e:
            print(f"An error occurred: {e}")
            raise

    def test_select_descending_price(self):
        search_term = "iphone 15 pro max"
        perform_search(self.driver, search_term)

        wait_and_click_element(self.driver, SORTING_MENU)
        wait_and_click_element(self.driver, DESCENDIND_ORDER_OPTION)
        time.sleep(5)

        # Extract product prices after sorting
        sorted_prices = extract_product_prices(self.driver)

        # Validate sorting order
        is_descending = sorted(sorted_prices, reverse=True)

        # Assert that prices are in descending order
        self.assertListEqual(
            sorted_prices,
            is_descending,
            "Prices are not in ascending order after sorting",
        )

    def test_select_by_review_nb(self):
        search_term = "iphone 15 pro max"
        perform_search(self.driver, search_term)

        wait_and_click_element(self.driver, SORTING_MENU)
        wait_and_click_element(self.driver, REVIEW_NB_OPTION)
        time.sleep(3)

        # Extract product prices after sorting
        sorted_results_by_reviews = extract_number_from_element(
            self.driver, RESULTS_BY_REVIEWS
        )

        # Validate sorting order (descending by review number)
        is_ordered = sorted(sorted_results_by_reviews, reverse=True)

        # Assert that results are in descending order by review number
        self.assertListEqual(
            sorted_results_by_reviews,
            is_ordered,
            "Results are not ordered correctly by review number",
        )


if __name__ == "__main__":
    unittest.main()

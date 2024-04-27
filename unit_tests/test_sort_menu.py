import time
import unittest
from sesiunea_11_12.tests.utils.setup import TestSetup
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
    RESULTS_BY_REVIEW_NB,
)


class SearchFunctionality(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = TestSetup.create_driver()
        cls.driver.get(URL)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_select_ascending_price(self):
        search_term = "caruta"
        perform_search(self.driver, search_term)

        wait_and_click_element(self.driver, SORTING_MENU)
        wait_and_click_element(self.driver, ASCENDING_ORDER_OPTION)

        # Extract product prices after sorting
        sorted_prices = extract_product_prices(self.driver)

        # Validate sorting order
        is_ascending = sorted(sorted_prices)

        # Assert that prices are in ascending order
        self.assertEqual(
            sorted_prices,
            is_ascending,
            "Prices are not in ascending order after sorting",
        )

    def test_select_descending_price(self):
        search_term = "caruta"
        perform_search(self.driver, search_term)

        wait_and_click_element(self.driver, SORTING_MENU)
        wait_and_click_element(self.driver, DESCENDIND_ORDER_OPTION)

        # Extract product prices after sorting
        sorted_prices = extract_product_prices(self.driver)

        # Validate sorting order
        is_descending = sorted(sorted_prices, reverse=True)

        # Assert that prices are in descending order
        self.assertEqual(
            sorted_prices,
            is_descending,
            "Prices are not in ascending order after sorting",
        )

    def test_select_by_review_nb(self):
        search_term = "caruta"
        perform_search(self.driver, search_term)

        wait_and_click_element(self.driver, SORTING_MENU)
        time.sleep(3)
        wait_and_click_element(self.driver, REVIEW_NB_OPTION)
        time.sleep(3)

        # Extract product prices after sorting
        sorted_results_by_review_nb = extract_number_from_element(
            self.driver, RESULTS_BY_REVIEW_NB
        )

        # Validate sorting order (descending by review number)
        is_ordered = sorted(sorted_results_by_review_nb, reverse=True)

        # Assert that results are in descending order by review number
        self.assertEqual(
            sorted_results_by_review_nb,
            is_ordered,
            "Results are not ordered correctly by review number",
        )


if __name__ == "__main__":
    unittest.main()

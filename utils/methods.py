import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from sesiunea_11_12.tests.utils.constants import (
    PRICES,
    SEARCH_BOX,
    SEARCH_BUTTON,
)


def wait_and_click_element(driver, locator):
    """Wait for an element to be clickable and then click it."""
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()
    time.sleep(3)


def perform_search(driver, search_term):
    search_box = driver.find_element(*SEARCH_BOX)
    search_box.clear()
    search_box.send_keys(search_term)
    search_button = driver.find_element(*SEARCH_BUTTON)
    search_button.click()


def extract_product_prices(driver):
    """
    Extracts prices from a webpage, splits them into main and decimal parts,
    stores them in a dictionary, and then formats the prices using the stored parts.

    Parameters:
        driver: Selenium WebDriver - The driver controlling the web browser.

    Returns:
        list of str: A list containing formatted prices as strings.
    """
    # time.sleep(3)
    price_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(PRICES)
    )

    # List to store formatted prices
    prices_as_float = []

    # Iterate through each price element
    for element in price_elements:
        # Extract the text of the price element
        price_text = (
            element.text.lower().replace("lei", "").strip()
        )  # Get the text and remove "lei" and extra whitespace

        # Split the price text into main and decimal parts
        main_part, _, decimal_part = price_text.partition(",")

        # Format the price using the main and decimal parts
        formatted_price = f"{main_part.replace('.', '')}.{decimal_part.strip()}"

        # Append formatted price to the list
        price_as_float = float(formatted_price)
        prices_as_float.append(price_as_float)

    return prices_as_float


def extract_number_from_element(driver, element):
    # Wait for the presence of all elements matching the provided locator

    # Find all elements matching the provided locator
    number_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(element)
    )

    # List to store extracted numbers
    numbers = []

    # Iterate through each element and extract the number
    for element in number_elements:
        # Get the text content of the element
        element_text = element.text.strip()

        # Skip processing if element text is empty
        if not element_text:
            continue  # Move to the next element

        # Handle non-empty element text
        # Replace certain characters and patterns in the element text
        cleaned_text = element_text.replace("(", "").replace(")", "").strip()

        try:
            # Convert the cleaned text to an integer
            element_value = int(cleaned_text)
            numbers.append(element_value)
        except ValueError:
            # Handle the case where the cleaned text cannot be converted to an integer
            print(
                f"Error converting to integer: '{cleaned_text}' is not a valid integer."
            )

    return numbers  # Return the list of extracted numbers

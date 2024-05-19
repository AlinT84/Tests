import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from sesiunea_11_12.tests.utils.constants import (
    SEARCH_BOX,
    SEARCH_BUTTON,
)


def wait_and_click_element(driver, locator):
    """Wait for an element to be clickable and then click it."""
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable(locator))
    element = wait.until(EC.visibility_of_element_located(locator))
    element.click()
    time.sleep(3)


def perform_search(driver, search_term):
    search_box = driver.find_element(*SEARCH_BOX)
    search_box.clear()
    search_box.send_keys(search_term)
    search_button = driver.find_element(*SEARCH_BUTTON)
    search_button.click()


def extract_data_from_elements(driver, locator, flow="default"):
    """
    Extracts data from web elements based on the provided locator and flow.

    Parameters:
        driver: The WebDriver instance controlling the browser.
        locator: A tuple representing the locator strategy (e.g., By.CSS_SELECTOR)
                         and the locator value (e.g., ".price").
        flow (optional): The specific flow for data extraction. Available options:
            - "default": Extracts raw text from elements.
            - "prices": Extracts prices, converts to float, and formats (removes "lei" and extra whitespace).
            - "numbers": Extracts numbers, removes parentheses, and converts to integer.

    Returns:
        A list containing extracted data (strings, floats, or integers).
    """
    # Wait for the presence of all elements matching the provided locator
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(locator)
    )

    # List to store extracted data
    extracted_data = []

    # Conditional logic based on the specified flow
    if flow == "prices":
        for element in elements:
            # Extract and process price data and remove "lei" and extra whitespace
            price_text = element.text.lower().replace("lei", "").strip()

            # Split the price text into main and decimal parts
            main_part, _, decimal_part = price_text.partition(",")

            # Format the price using the main and decimal parts (as float)
            formatted_price = f"{main_part.replace('.', '')}.{decimal_part.strip()}"
            try:
                price_value = float(formatted_price)
                extracted_data.append(price_value)
            except ValueError:
                print(f"Error converting price to float: '{price_text}'")
    elif flow == "numbers":
        for element in elements:
            # Extract and process number data
            # Example specific processing for numbers (remove parentheses and convert to int)
            number_text = element.text.strip().replace("(", "").replace(")", "")
            try:
                number_value = int(number_text)
                extracted_data.append(number_value)
            except ValueError:
                print(f"Error converting number to int: '{number_text}'")
    else:
        # Default flow: extract raw text from elements
        for element in elements:
            # Extract raw text data
            extracted_data.append(element.text.strip())

    return extracted_data  # Return the list of extracted data

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sesiunea_11_12.tests.utils.constants import (
    PRODUCT_PRICES_ELEMENT,
    SEARCH_BOX,
    SEARCH_BUTTON,
)


def wait_and_click_element(driver, locator):
    """Wait for an element to be clickable and then click it."""
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


def perform_search(driver, search_term):
    search_box = driver.find_element(*SEARCH_BOX)
    search_box.clear()
    search_box.send_keys(search_term)
    search_button = driver.find_element(*SEARCH_BUTTON)
    search_button.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(PRODUCT_PRICES_ELEMENT)
    )


def extract_product_prices(driver):
    try:
        # Wait for the presence of all elements matching the provided locator
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PRODUCT_PRICES_ELEMENT)
        )

        # Find all elements matching the provided locator
        price_elements = driver.find_elements(*PRODUCT_PRICES_ELEMENT)

        # List to store extracted prices
        prices = []

        # Iterate through each element and extract the price
        for element in price_elements:
            # Get the text content of the element and preprocess it
            price_text = (
                element.text # Remove leading and trailing whitespace
                .replace(".", "")  # Remove thousands separator
                .replace(",", ".")  # Replace decimal separator with dot (for float conversion)
            )

            # Check if the price text is empty or invalid
            if not price_text:
                continue  # Skip empty price texts

            try:
                # Convert the preprocessed price text to a float value
                price_value = float(price_text)
                prices.append(
                    price_value
                )  # Append the converted price to the list of prices
            except ValueError:
                # Handle the case where price text cannot be converted to float
                print(
                    f"Error converting price: '{price_text}' is not a valid float value"
                )

        return prices  # Return the list of extracted prices

    except Exception as e:
        # Handle any exceptions that might occur during element extraction
        print(f"Error extracting prices: {e}")
        return []


def extract_number_from_element(driver, element):
    try:
        # Wait for the presence of all elements matching the provided locator
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(element))

        # Find all elements matching the provided locator
        number_elements = driver.find_elements(*element)

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

    except Exception as e:
        # Handle any exceptions that might occur during element extraction
        print(f"Error extracting numbers: {e}")
        return []  # Return an empty list in case of error

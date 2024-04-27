from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .constants import (
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
    return driver.find_elements(*PRODUCT_PRICES_ELEMENT)


def extract_product_prices(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(PRODUCT_PRICES_ELEMENT)
    )
    price_elements = driver.find_elements(*PRODUCT_PRICES_ELEMENT)
    prices = []
    for element in price_elements:
        price_text = (
            element.text.strip()
            .lower()
            .replace("lei", "")
            .replace(".", "")
            .replace(",", ".")
            .strip()
        )
        try:
            price_value = float(price_text)
            prices.append(price_value)
        except ValueError:
            print(f"Error converting price: {price_text}")
    return prices


def extract_number_from_element(driver, element):
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(element))
    number_elements = driver.find_elements(*element)
    numbers = []
    for element in number_elements:
        try:
            element_value = int(element)
            numbers.append(element_value)
        except ValueError:
            print(f"Error converting price: {price_text}")

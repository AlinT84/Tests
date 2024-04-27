from selenium.webdriver.common.by import By

URL = "https://www.emag.ro/"

# Elements
COOKIES_BUTTON = (By.XPATH, '//button[contains(text(),"Accept toate")]')
LOGIN_X_BUTTON = (By.XPATH, '//button/i[@class="em em-close"]')
SEARCH_BOX = (By.ID, "searchboxTrigger")
SEARCH_BUTTON = (By.CLASS_NAME, "searchbox-submit-button")
SORTING_MENU = (By.CSS_SELECTOR, ".sort-control-btn")
ASCENDING_ORDER_OPTION = (By.XPATH, '//a[text()="Pret crescator"]')
DESCENDIND_ORDER_OPTION = (By.XPATH, '//a[text()="Pret descrescator"]')
REVIEW_NB_OPTION = (By.CLASS_NAME, "Nr. review-uri")
RESULTS_BY_REVIEW_NB = (By.CLASS_NAME, "visible-xs-inline-block ")
PRODUCT_PRICES_ELEMENT = (By.XPATH, '//div/p[@class="product-new-price"]')

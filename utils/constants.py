from selenium.webdriver.common.by import By

URL = "https://www.emag.ro/"

# Elements
MAIN_PAGE_LOGO_BUTTON = (By.XPATH, '//img[@alt="eMAG"]')
ACCOUNT_BUTTON = (By.XPATH, '//a[@id="my_account"]')
FAV_BUTTON = (By.XPATH, '//a[@id="my_wishlist"]')
CART_BUTTON = (By.XPATH, '//a[@id="my_cart"]')
GENIUS_DEALS_BUTTON = (
    By.XPATH,
    '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Genius Deals"]',
)
GENIUS_BUTTON = (
    By.XPATH,
    '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Genius"]',
)
CARD_IDEI_BUTTON = (
    By.XPATH,
    '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Cardul cu milioane de idei"]',
)
RABLA_BUTTON = (
    By.XPATH,
    '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Rabla"]',
)
OFERTE_EMAG_BUTTON = (
    By.XPATH,
    '//ul[@class="nav navbar-nav navbar-left "]/li/a[@title="Ofertele eMAG"]',
)
COOKIES_BUTTON = (By.XPATH, '//button[contains(text(),"Accept toate")]')
LOGIN_X_BUTTON = (By.XPATH, '//button/i[@class="em em-close"]')
SEARCH_BOX = (By.ID, "searchboxTrigger")
SEARCH_BUTTON = (By.CLASS_NAME, "searchbox-submit-button")
SORTING_MENU = (By.CSS_SELECTOR, ".sort-control-btn")
ASCENDING_ORDER_OPTION = (By.XPATH, '//a[text()="Pret crescator"]')
DESCENDIND_ORDER_OPTION = (By.XPATH, '//a[text()="Pret descrescator"]')
REVIEW_NB_OPTION = (By.XPATH, '//a[text()="Nr. review-uri"]')
RESULTS_BY_REVIEWS = (By.XPATH, '//span[@class="visible-xs-inline-block "]')
PRICES = (
    By.XPATH,
    '//div[@class="page-container"]/descendant::p[@class="product-new-price"]',
)

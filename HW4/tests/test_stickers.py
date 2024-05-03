from base_functions import get_elements
from selenium.webdriver.common.by import By


def test_stickers(driver):
    driver.get("http://localhost/litecart")

    products = get_elements(driver, (By.CSS_SELECTOR, '.content .product .link'))

    for product in products:
        stickers = get_elements(product, (By.CSS_SELECTOR, '.sticker'))
        assert len(stickers) == 1

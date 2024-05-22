from base_functions import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


LOCATOR_QUANTITY = (By.CSS_SELECTOR, '#cart-wrapper #cart .quantity')
LOCATOR_BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button[value="Add To Cart"]')
LOCATOR_SELECT_OPTION_SIZE = (By.CSS_SELECTOR, '.options select[name="options[Size]"]')


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_product_count(self):
        quantity = self.get_element(LOCATOR_QUANTITY)
        return int(quantity.get_attribute('textContent'))

    def add_product_to_cart(self):
        start_count = self.get_cart_product_count()

        button = self.get_element(LOCATOR_BUTTON_ADD_TO_CART)
        options = self.get_element(LOCATOR_SELECT_OPTION_SIZE, 1)
        if options:
            select = Select(options)
            select.select_by_value("Small")
        button.click()

        g = self.get_element((By.XPATH, f'//*[@id="cart"]/a[2]/span[@class="quantity" and contains(text(), "{start_count + 1}")]'))
        return g




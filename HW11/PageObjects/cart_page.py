from base_functions import BasePage
from selenium.webdriver.common.by import By


LOCATOR_REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[name="remove_cart_item"]')
LOCATOR_PRODUCTS_TABLE = (By.CSS_SELECTOR, '#order_confirmation-wrapper tbody tr:not(.header) .item')
LOCATOR_CART = (By.CSS_SELECTOR, '#cart')


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_cart_page(self):
        self.get_element(LOCATOR_CART).click()

    def delete_product(self, elem):
        b = self.get_element(LOCATOR_REMOVE_BUTTON)
        b.click()
        self.wait_element_disappearance(b)
        return self.wait_element_disappearance(elem)

    def get_products_from_table(self):
        return self.get_elements(LOCATOR_PRODUCTS_TABLE)


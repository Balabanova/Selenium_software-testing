from base_functions import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_main_page(self):
        self.driver.get("http://localhost/litecart/en/")

    def go_to_most_popular_product(self, nth):
        product = self.get_element((By.CSS_SELECTOR, f"#box-most-popular li.product:nth-child({nth})"))
        product.click()
        return product

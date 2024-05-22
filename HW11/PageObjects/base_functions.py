from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                        message=f"Can't find elements by locator {locator}")
        except TimeoutException as e:
            return None
        except NoSuchElementException as e:
            return None

    def get_elements(self, locator, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                        message=f"Can't find elements by locator {locator}")
        except TimeoutException as e:
            return []
        except NoSuchElementException as e:
            return []

    def wait_element_disappearance(self, element, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.staleness_of(element))
        except TimeoutException as e:
            return False

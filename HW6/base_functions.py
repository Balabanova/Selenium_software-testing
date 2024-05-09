from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def get_element(driver, locator, timeout=5):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator),
                                                    message=f"Can't find elements by locator {locator}")
    except TimeoutException as e:
        return None
    except NoSuchElementException as e:
        return None


def get_elements(driver, locator, timeout=5):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                    message=f"Can't find elements by locator {locator}")
    except TimeoutException as e:
        return []
    except NoSuchElementException as e:
        return []

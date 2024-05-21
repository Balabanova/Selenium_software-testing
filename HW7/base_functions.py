from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_element_disappearance(driver, element, timeout=5):
    try:
        c = WebDriverWait(driver, timeout).until(EC.staleness_of(element))
        return c
    except TimeoutException as e:
        return False


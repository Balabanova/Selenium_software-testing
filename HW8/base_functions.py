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


def wait_window(driver, old_count, timeout=5):
    WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(old_count+1))


def get_new_window(driver, old_windows):
    wait_window(driver, len(old_windows))
    for window_handle in driver.window_handles:
        if window_handle not in old_windows:
            new_window = window_handle
            return new_window
    return None

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator),
                                                message=f"Can't find elements by locator {locator}")


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    username_input = get_element(driver, (By.CSS_SELECTOR, 'input[name="username"]'))
    username_input.send_keys("admin")
    password_input = get_element(driver, (By.CSS_SELECTOR, 'input[name="password"]'))
    password_input.send_keys("admin")
    login_button = get_element(driver, (By.CSS_SELECTOR, 'button[name = "login"]'))
    login_button.click()



import pytest
from base_functions import get_element
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    _browser = webdriver.Chrome()
    yield _browser
    _browser.quit()


@pytest.fixture(scope="function")
def login_to_admin(driver):
    driver.get("http://localhost/litecart/admin/")
    username_input = get_element(driver, (By.CSS_SELECTOR, 'input[name="username"]'))
    username_input.send_keys("admin")
    password_input = get_element(driver, (By.CSS_SELECTOR, 'input[name="password"]'))
    password_input.send_keys("admin")
    login_button = get_element(driver, (By.CSS_SELECTOR, 'button[name = "login"]'))
    login_button.click()

from base_functions import get_element, get_elements
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("login_to_admin")
def test_login(driver):
    apps = get_elements(driver, (By.CSS_SELECTOR, 'ul#box-apps-menu li#app-'))

    for app in range(1, len(apps)+1):
        app = get_element(driver, (By.CSS_SELECTOR, f'ul#box-apps-menu li#app-:nth-child({app})'))
        app.click()

        app_childes = get_elements(driver, (By.CSS_SELECTOR, 'ul.docs li[id^="doc-"]'), 3)
        if app_childes:
            for app_cild in range(1, len(app_childes)+1):
                app = get_element(driver, (By.CSS_SELECTOR, f'ul.docs li[id^="doc-"]:nth-child({app_cild})'))
                app.click()
                assert get_element(driver, (By.CSS_SELECTOR, '#content h1'))
        else:
            get_element(driver, (By.CSS_SELECTOR, '#content h1'))

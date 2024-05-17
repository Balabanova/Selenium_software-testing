import pytest
from base_functions import get_elements, get_element
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("login_to_admin")
def test_logs(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    products = get_elements(driver, (By.CSS_SELECTOR, ".row td:nth-child(3) img + a"))
    for p in range(0, len(products)):
        get_elements(driver, (By.CSS_SELECTOR, ".row td:nth-child(3) img + a"))[p].click()
        logs = driver.get_log("browser")
        assert len(logs) == 0, logs
        get_element(driver, (By.CSS_SELECTOR, 'button[name="cancel"]')).click()


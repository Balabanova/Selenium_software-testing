from base_functions import get_element, get_elements
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("login_to_admin")
def test_country_order(driver):
    driver.get(" http://localhost/litecart/admin/?app=countries&doc=countries")

    rows = get_elements(driver, (By.CSS_SELECTOR, 'tbody .row'))
    last_country_name = ""
    country_zone_list = []
    for row in rows:
        country = get_element(row, (By.CSS_SELECTOR, 'td:nth-child(5) a'))
        country_name = country.get_attribute('textContent')
        assert country_name >= last_country_name

        country_zone = get_elements(row, (By.CSS_SELECTOR, 'td:nth-child(6)'))
        country_zone_num = country_zone[0].get_attribute('textContent')
        if country_zone_num is not "0":
            country_zone_list.append(country_name)

    for l in country_zone_list:
        zone = get_element(driver, (By.XPATH, f'.//table[@class="dataTable"]//a[contains(text(), "{l}")]'))
        zone.click()

        ch_rows = get_elements(driver, (By.CSS_SELECTOR, 'tbody .row'))
        last_ch_country_name = ""
        for ch_row in ch_rows:
            ch_country = get_element(ch_row, (By.CSS_SELECTOR, 'td:nth-child(5) '))
            ch_country_name = ch_country.get_attribute('textContent')
            assert ch_country_name >= last_ch_country_name

        cancel = get_element(driver, (By.CSS_SELECTOR, "button[name='cancel']"))
        cancel.click()

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    _browser = webdriver.Chrome()
    yield _browser
    _browser.quit()


def test_open_browser(driver):
    driver.get("https://www.google.ru/")

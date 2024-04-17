import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    _browser = webdriver.Chrome()
    yield _browser
    _browser.quit()

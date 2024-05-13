import pytest
from selenium.webdriver.common.by import By
from base_functions import get_elements, get_new_window


@pytest.mark.usefixtures("login_to_admin")
def test_new_window(driver):
    # Переходим на страницу редактированиея страны
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    edit_buttons = get_elements(driver, (By.CSS_SELECTOR, "table.dataTable .row td:nth-child(7)"))
    edit_buttons[0].click()

    # Запоминаем идентификатор текущей страницы
    country_window = driver.current_window_handle

    # Получаем все элементы с внешними ссылками
    links = get_elements(driver, (By.CSS_SELECTOR, ".fa-external-link"))
    for i in range(0, len(links)):
        # Запоминаем кол-во открытых окон до открытия нового
        old_windows = driver.window_handles
        # Открываем новое окно
        links[i].click()
        # Вызываем функцию, включающую ожидание окна и поиск нового идентификатора, который передаем в переменную
        new_window = get_new_window(driver, old_windows)
        assert new_window
        # Переключаемся на новое окно
        driver.switch_to.window(new_window)
        # Закрываем новое окно
        driver.close()
        # Возвращаемся в главное окно
        driver.switch_to.window(country_window)


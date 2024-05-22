from base_functions import wait_element_disappearance
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def get_items_from_table(driver):
    return driver.find_elements(By.CSS_SELECTOR, '#order_confirmation-wrapper tbody tr:not(.header) .item')


def test_cart(driver):
    driver.implicitly_wait(3)

    for i in range(3):
        # Переходим на главную страницу
        driver.get("http://localhost/litecart/en/")
        # Переходим в карточку первого из популярных товара
        driver.find_element(By.CSS_SELECTOR, "#box-most-popular li.product:first-child").click()
        # Добавляем товар в корзину
        button = driver.find_element(By.CSS_SELECTOR, 'button[value="Add To Cart"]')
        button.click()
        # Получаем элемент корзины, если товаров в ней на 1 больше, чем было
        g = driver.find_elements(By.XPATH, f'//*[@id="cart"]/a[2]/span[@class="quantity" and contains(text(), "{i+1}")]')
        # Если количество товара в корзине не соответствует предыдущему условию,
        # проверяем товар на наличие дополнительных и обязательных к заполнению опций
        if not g:
            options = driver.find_element(By.CSS_SELECTOR, '.options select[name="options[Size]"]')
            # Устанавливаем значение опции
            if options:
                select = Select(options)
                select.select_by_value("Small")
            button.click()
            # Еще раз получаем элемент корзины
            g = driver.find_elements(By.XPATH, f'//*[@id="cart"]/a[2]/span[@class="quantity" and contains(text(), "{i + 1}")]')
        # Проверяем, что элемент корзины с верным числом товаров в ней найден
        assert g[0]

    # Переходим в карзину
    driver.find_element(By.CSS_SELECTOR, "#cart").click()
    # Находи все элементы, содержащиеся в строках таблицы заказа
    items_count = len(get_items_from_table(driver))
    # Поочередно удаляем товары из корзины и проверяем, что таблица заказа обновилась
    for i in range(0, items_count):
        item = get_items_from_table(driver)[0]
        b = driver.find_element(By.CSS_SELECTOR, 'button[name="remove_cart_item"]')
        b.click()
        wait_element_disappearance(driver, b)
        assert wait_element_disappearance(driver, item)

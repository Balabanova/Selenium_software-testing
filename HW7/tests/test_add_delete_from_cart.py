from base_functions import wait_element_disappearance
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base_functions import get_elements, get_element


def get_items_from_table(driver):
    return get_elements(driver, (By.CSS_SELECTOR, '#order_confirmation-wrapper tbody tr:not(.header) .item'))


def test_cart(driver):
    driver.implicitly_wait(0)
    for i in range(3):
        # Переходим на главную страницу
        driver.get("http://localhost/litecart/en/")
        # Переходим в карточку первого из популярных товара
        get_element(driver, (By.CSS_SELECTOR, "#box-most-popular li.product:first-child")).click()

        button = get_element(driver, (By.CSS_SELECTOR, 'button[value="Add To Cart"]'))
        # Проверяем товар на наличие дополнительных и обязательных к заполнению опций
        options = get_element(driver, (By.CSS_SELECTOR, '.options select[name="options[Size]"]'), 1)
        if options:
            # Устанавливаем значение опции
            select = Select(options)
            select.select_by_value("Small")
        # Добавляем товар в корзину
        button.click()
        g = get_elements(driver, (By.XPATH, f'//*[@id="cart"]/a[2]/span[@class="quantity" and contains(text(), "{i + 1}")]'))
        # Проверяем, что элемент корзины с верным числом товаров в ней найден
        assert g[0]

    # Переходим в карзину
    get_element(driver, (By.CSS_SELECTOR, "#cart")).click()
    # Находи все элементы, содержащиеся в строках таблицы заказа
    items_count = len(get_items_from_table(driver))
    # Поочередно удаляем товары из корзины и проверяем, что таблица заказа обновилась
    for i in range(0, items_count):
        item = get_items_from_table(driver)[0]
        b = get_element(driver, (By.CSS_SELECTOR, 'button[name="remove_cart_item"]'))
        b.click()
        wait_element_disappearance(driver, b)
        assert wait_element_disappearance(driver, item)

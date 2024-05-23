from base_functions import get_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest
import os


@pytest.mark.usefixtures("login_to_admin")
def test_add_new_product(driver):
    # Переходим в каталог
    get_element(driver, (By.XPATH, '//*[@id="app-"]//span[contains(text(), "Catalog")]')).click()
    # Переходим на страницу добавления продукта
    get_element(driver, (By.XPATH, '//*[@id="content"]//a[@class="button"] [contains(text(), " Add New Product")] ')).click()

    # GENERAL
    # Чек на доступности товара
    get_element(driver, (By.CSS_SELECTOR, '#tab-general input[name="status"][value="1"]')).click()
    # Генерируем и заполняем имя товара
    pr_name = "product" + str(time.time())
    get_element(driver, (By.CSS_SELECTOR, '#tab-general .input-wrapper input')).send_keys(pr_name)
    # Генерируем и заполняем код товара
    get_element(driver, (By.CSS_SELECTOR, 'input[name="code"]')).send_keys(str(time.time()))
    # Выбираем группу товара
    get_element(driver, (By.CSS_SELECTOR, '.input-wrapper input[type="checkbox"][name="product_groups[]"][value="1-3"]')).click()
    # Заполняем количество товара
    g = get_element(driver, (By.CSS_SELECTOR, 'input[name="quantity"]'))
    g.clear()
    g.send_keys("5")
    # Загружаем изображение товара
    get_element(driver, (By.CSS_SELECTOR, 'input[name="new_images[]"]')).send_keys(os.getcwd() + "\img.jpg")
    # Заполняем даты валидности товара
    get_element(driver, (By.CSS_SELECTOR, 'input[name="date_valid_from"]')).send_keys("23052024")
    get_element(driver, (By.CSS_SELECTOR, 'input[name="date_valid_to"]')).send_keys("23052025")

    # Переходим на вкладку Info
    get_element(driver, (By.XPATH, './/a[contains(text(), "Information")]')).click()

    # INFO
    # Выбираем производителя товара
    select = Select(get_element(driver, (By.CSS_SELECTOR, 'select[name="manufacturer_id"]')))
    select.select_by_value("1")
    # Заполняем ключевые слова
    get_element(driver, (By.CSS_SELECTOR, 'input[name="keywords"]')).send_keys("my_test")
    # Заполняем короткое описание
    get_element(driver, (By.CSS_SELECTOR, 'input[name="short_description[en]"]')).send_keys("my_test")
    # Заполняем полное описание
    get_element(driver, (By.CSS_SELECTOR, '.trumbowyg-editor')).send_keys("my_test\ndescription")
    # Заполняем заголовок
    get_element(driver, (By.CSS_SELECTOR, 'input[name="head_title[en]"]')).send_keys(pr_name)
    # Заполняем еще одно описание
    get_element(driver, (By.CSS_SELECTOR, 'input[name="meta_description[en]"]')).send_keys("my_test")

    # Переходим на вкладку Prices
    get_element(driver, (By.XPATH, './/a[contains(text(), "Prices")]')).click()

    # PRICES
    # Заполняем покупочную цену
    p = get_element(driver, (By.CSS_SELECTOR, 'input[name="purchase_price"]'))
    p.clear()
    p.send_keys("30.5")
    # Выбираем валюту
    select = Select(get_element(driver, (By.CSS_SELECTOR, 'select[name="purchase_price_currency_code"]')))
    select.select_by_value("USD")
    # Заполняем цену в долларах
    get_element(driver, (By.CSS_SELECTOR, 'input[name="prices[USD]"]')).send_keys("40")
    # Заполняем цену в евро
    get_element(driver, (By.CSS_SELECTOR, 'input[name="prices[EUR]"]')).send_keys("30")

    # Сохраняем товар
    get_element(driver, (By.CSS_SELECTOR, 'button[name="save"]')).click()

    # Проверяем наличие нового товара в списке
    assert get_element(driver, (By.XPATH, f'.//a[contains(text(), "{pr_name}")]'))




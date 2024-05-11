from base_functions import get_element
from selenium.webdriver.common.by import By
import re
import pytest


def get_prices_info(product):
    """
    For getting info about regular and campaign prices (text, size, color_type, color)
    :param product: element containing a regular and a campaign prices
    :return: diction for regular and campaign prices. Format: {text, size, color_type, color}
    """
    # (ПРОВЕРКА В) Пытаемся найти <s> элемент (зачеркнутый текст)
    reg_price = get_element(product, (By.CSS_SELECTOR, '.price-wrapper s.regular-price'))
    if not reg_price:
        pytest.fail("Элемент 'Обычная цена (зачеркнутый текст)' не найден")
    reg_price_text = reg_price.get_attribute('textContent')
    reg_price_int = float(re.sub("[$|€]", "", reg_price_text))
    reg_price_color = reg_price.value_of_css_property('color')
    r_color_type, r_color = get_color(reg_price_color)
    reg_price_size_text = reg_price.value_of_css_property('font-size')
    reg_price_size = float(re.sub("px", "", reg_price_size_text))

    # (ПРОВЕРКА Г) Пытаемся найти <strong> элемент (жирный шрифт)
    camp_price = get_element(product, (By.CSS_SELECTOR, '.price-wrapper strong.campaign-price'))
    if not camp_price:
        pytest.fail("Элемент 'Акционная цена (жирный шрифт)' не найден")
    camp_price_text = camp_price.get_attribute('textContent')
    camp_price_int = float(re.sub("[$|€]", "", camp_price_text))
    camp_price_color = camp_price.value_of_css_property('color')
    c_color_type, c_color = get_color(camp_price_color)
    camp_price_size_text = camp_price.value_of_css_property('font-size')
    camp_price_size = float(re.sub("px", "", camp_price_size_text))

    return {"reg_text": reg_price_int, "reg_size": reg_price_size, "reg_color_type": r_color_type, "reg_color": r_color}, \
           {"camp_text": camp_price_int, "camp_size": camp_price_size, "camp_color_type": c_color_type, "camp_color": c_color}


def get_color(color):
    patt_rgba = r"rgba\((\d{1,3}), (\d{1,3}), (\d{1,3}), (\d{1})\)"
    patt_rgb = r"rgba\((\d{1,3}), (\d{1,3}), (\d{1,3})\)"
    patt_hex = r"#(\d{6})"

    rgba_s = re.search(patt_rgba, color)
    rgb_s = re.search(patt_rgb, color)
    hex_s = re.search(patt_hex, color)

    if rgba_s:
        return "rgba", [rgba_s.group(1), rgba_s.group(2), rgba_s.group(3), rgba_s.group(4)]
    elif rgb_s:
        return "rgb", [rgb_s.group(1), rgb_s.group(2), rgb_s.group(3)]
    elif hex_s:
        return "hex", hex_s.group(1)


def check_grey_color(color_type, color):
    if color_type == "rgb" or color_type == "rgba":
        assert color[0] == color[1] == color[2]
    elif color_type == "hex":
        print("Я не знаю как здесь проверить серость")


def check_red_color(color_type, color):
    if color_type == "rgb" or color_type == "rgba":
        assert color[1] == color[2] == "0"
    elif color_type == "hex":
        print("Я не знаю как здесь проверить красность")


def test_check_styles(driver):
    driver.get("http://localhost/litecart/en/")

    # Получаем карточку продукта по скидке
    campaign_product = get_element(driver, (By.CSS_SELECTOR, '#box-campaigns li:nth-child(1) .link'))
    # Получаем название продукта из карточки
    c_name_text = get_element(campaign_product, (By.CSS_SELECTOR, '.name')).get_attribute('textContent')
    # Получаем информацию об обычной цене и акционной
    c_reg_price, c_camp_price = get_prices_info(campaign_product)

    # (ПРОВЕРКИ В Г) Проверяем , что обычная цена - серая, а акционная - красная
    check_grey_color(c_reg_price["reg_color_type"], c_reg_price["reg_color"])
    check_red_color(c_camp_price["camp_color_type"], c_camp_price["camp_color"])

    # Проверяем, что обычная цена выше акционной
    assert c_reg_price["reg_text"] > c_camp_price["camp_text"]
    # (ПРОВЕРКА Д) Проверяем, что шрифт обычной цены меньше, чем акционной
    assert c_reg_price["reg_size"] < c_camp_price["camp_size"]

    # Переходим на страницу продукта
    campaign_product.click()

    # Получаем блок продукта
    box_product = get_element(driver, (By.CSS_SELECTOR, '#box-product'))
    # Получаем название продукта из блока
    r_name_text = get_element(box_product, (By.CSS_SELECTOR, '#box-product h1')).get_attribute('textContent')
    # Получаем информацию об обычной цене и акционной
    p_reg_price, p_camp_price = get_prices_info(box_product)

    # (ПРОВЕРКИ В Г) Проверяем , что обычная цена - серая, а акционная - красная
    check_grey_color(p_reg_price["reg_color_type"], p_reg_price["reg_color"])
    check_red_color(p_camp_price["camp_color_type"], p_camp_price["camp_color"])

    # Проверяем, что обычная цена выше акционной
    assert p_reg_price["reg_text"] > p_camp_price["camp_text"]
    # (ПРОВЕРКА Д) Проверяем, что шрифт обычной цены меньше, чем акционной
    assert p_reg_price["reg_size"] < p_camp_price["camp_size"]

    # (ПРОВЕРКА А) Проверяем, что названия продукта на главной странице и в карточке товара совпадают
    assert c_name_text == r_name_text
    # (ПРОВЕРКА Б) Проверяем, что обычные цены на главной странице и в карточке товара совпадают
    assert c_reg_price["reg_text"] == p_reg_price["reg_text"]
    # (ПРОВЕРКА Б) Проверяем, что акцтонные цены на главной странице и в карточке товара совпадают
    assert c_camp_price["camp_text"] == p_camp_price["camp_text"]

from base_functions import get_element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import string


def generate_random_num():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))


def test_add_new_user(driver):
    driver.get("http://localhost/litecart/en/")

    # Переходим по линку на страницу регистрации нового пользователя
    get_element(driver, (By.XPATH, ".// a[contains(text(), 'New customers click here')]")).click()

    # Заполняем поля регистрации:
    # Имя (10 рандомных символов)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="firstname"]')).send_keys(generate_random_num())
    # Фамилия (10 рандомных символов)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="lastname"]')).send_keys(generate_random_num())
    # Адрес (10 рандомных символов)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="address1"]')).send_keys(generate_random_num())
    # Индекс (рандомное 5-значное число)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="postcode"]')).send_keys(random.randint(10000, 99999))
    # Город (10 рандомных символов)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="city"]')).send_keys(generate_random_num())

    # Страна (США)
    country = get_element(driver, (By.CSS_SELECTOR, 'span.selection'))
    ActionChains(driver).click(country).send_keys("United States").send_keys(Keys.ENTER).perform()

    # Штат (Аляска)
    select = Select(get_element(driver, (By.CSS_SELECTOR, 'select[name="zone_code"]')))
    select.select_by_value("AK")

    # Email (10 рандомных символов + @gmail.com)
    email = generate_random_num()+"@gmail.com"
    get_element(driver, (By.CSS_SELECTOR, 'input[name="email"]')).send_keys(email)

    # Телефон (+1 + рандомное 5-значнное число)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="phone"]')).send_keys("+1"+str(random.randint(10000, 99999)))

    # Пароль и подтверждение пароля (10 рандомных символов)
    password = generate_random_num()
    get_element(driver, (By.CSS_SELECTOR, 'input[name="password"]')).send_keys(password)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="confirmed_password"]')).send_keys(password)

    # Подтверждение регистрации
    get_element(driver, (By.CSS_SELECTOR, 'button[name="create_account"]')).click()

    # Выходим из аккаунта
    get_element(driver, (By.XPATH, '.// a[contains(text(), "Logout")]')).click()

    # Вводим Email , пароль нового пользователя и входим в аккаунт
    get_element(driver, (By.CSS_SELECTOR, 'input[name="email"]')).send_keys(email)
    get_element(driver, (By.CSS_SELECTOR, 'input[name="password"]')).send_keys(password)
    get_element(driver, (By.CSS_SELECTOR, 'button[name="login"]')).click()

    # Выходим из аккаунта
    get_element(driver, (By.XPATH, './/a[contains(text(), "Logout")]')).click()







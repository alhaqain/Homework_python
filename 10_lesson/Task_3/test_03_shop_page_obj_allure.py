import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from LoginPageAllure import LoginPage
from InventoryPageAllure import InventoryPage
from CartPageAllure import CartPage
from CheckoutPageAllure import CheckoutPage


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и закрытия браузера Firefox.

    :return: WebDriver — экземпляр драйвера Firefox.
    """
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест оформления заказа")
@allure.description("Авторизация, добавление товаров, "
                    "переход к оформлению и проверка итоговой суммы.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_total_sum_page_object(driver):
    login_page = LoginPage(driver)
    with allure.step("Открытие страницы логина и авторизация"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    with allure.step("Добавление товаров в корзину"):
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        for item_id in items_to_add:
            inventory_page.add_item_to_cart(item_id)
        inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    with allure.step("Переход к оформлению заказа"):
        cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    with allure.step("Заполнение формы покупателя"):
        checkout_page.fill_form("Иван", "Петров", "123456")

    with allure.step("Получение итоговой суммы"):
        total_value = checkout_page.get_total()

    with allure.step("Проверка итоговой суммы: ожидаем '$58.29', "
                     "получено {total_value}"):
        assert total_value == "$58.29"

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_total_sum_page_object(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    items_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for item_id in items_to_add:
        inventory_page.add_item_to_cart(item_id)
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Петров", "123456")
    total_value = checkout_page.get_total()

    assert total_value == "$58.29"

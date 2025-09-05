from selenium.webdriver.common.by import By
import allure


class InventoryPage:
    def __init__(self, driver):
        """
        Класс для работы со страницей списка товаров.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление товара в корзину (ID: {item_id})")
    def add_item_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его ID.

        :param item_id: str — идентификатор кнопки добавления товара.
        """
        self.driver.find_element(By.ID, item_id).click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        self.driver.find_element(*self.cart_button).click()

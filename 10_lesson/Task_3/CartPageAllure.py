from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        """
        Класс для работы со страницей корзины.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Переход к оформлению заказа")
    def proceed_to_checkout(self) -> None:
        """
        Нажимает кнопку перехода к оформлению заказа.
        """
        self.driver.find_element(*self.checkout_button).click()

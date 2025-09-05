from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    def __init__(self, driver):
        """
        Класс для работы со страницей оформления заказа.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнение формы покупателя: {first} {last}, {postal}")
    def fill_form(self, first: str, last: str, postal: str) -> None:
        """
        Заполняет форму данными покупателя и нажимает 'Continue'.

        :param first: str — имя покупателя.
        :param last: str — фамилия покупателя.
        :param postal: str — почтовый индекс.
        """
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получение итоговой суммы заказа")
    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: str — итоговая сумма заказа (например, "32.39").
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_label)
        )
        return total_element.text.replace("Total: ", "").strip()

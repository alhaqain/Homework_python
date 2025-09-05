from selenium.webdriver.common.by import By
import allure


class FormPage:
    def __init__(self, driver):
        """
        Класс для работы со страницей формы.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = ("https://bonigarcia.dev/"
                    "selenium-webdriver-java/data-types.html")

        self.fields = {
            "first-name": (By.NAME, "first-name"),
            "last-name": (By.NAME, "last-name"),
            "address": (By.NAME, "address"),
            "e-mail": (By.NAME, "e-mail"),
            "phone": (By.NAME, "phone"),
            "zip-code": (By.NAME, "zip-code"),
            "city": (By.NAME, "city"),
            "country": (By.NAME, "country"),
            "job-position": (By.NAME, "job-position"),
            "company": (By.NAME, "company"),
        }

        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    @allure.step("Открытие страницы формы")
    def open(self) -> None:
        """
        Открывает страницу формы.
        """
        self.driver.get(self.url)

    @allure.step("Заполнение поля '{field_name}' значением '{value}'")
    def fill_field(self, field_name: str, value: str) -> None:
        """
        Заполняет указанное поле формы.

        :param field_name: str — имя поля (ключ из словаря self.fields).
        :param value: str — значение для ввода.
        :return: None
        """
        element = self.driver.find_element(*self.fields[field_name])
        element.clear()
        element.send_keys(value)

    @allure.step("Отправка формы")
    def submit(self) -> None:
        """
        Нажимает кнопку отправки формы.
        """
        self.driver.find_element(*self.submit_button).click()

    @allure.step("Получение цвета текста поля '{field_id}'")
    def get_color(self, field_id: str) -> str:
        """
        Возвращает CSS-свойство 'color' для указанного поля.

        :param field_id: str — ID поля формы.
        :return: str — цвет текста (например, 'rgba(255, 0, 0, 1)').
        """
        return self.driver.find_element(
            By.CSS_SELECTOR, f'#{field_id}'
        ).value_of_css_property("color")

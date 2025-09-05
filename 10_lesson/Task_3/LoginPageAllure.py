from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Класс для работы со страницей авторизации.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """
        Открывает страницу логина.
        """
        self.driver.get(self.url)

    @allure.step("Авторизация: {username} / {password}")
    def login(self, username: str, password: str) -> None:
        """
        Ввод логина и пароля, затем вход в систему.

        :param username: str — имя пользователя.
        :param password: str — пароль.
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

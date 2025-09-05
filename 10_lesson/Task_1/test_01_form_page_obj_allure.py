import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from FormPageAllure import FormPage


@pytest.fixture()
def driver():
    """
    Фикстура для запуска и закрытия браузера Edge.

    :return: WebDriver — экземпляр драйвера Edge.
    """
    service = EdgeService(executable_path=r"msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.step("Проверка, что поле 'zip-code' подсвечено красным")
def check_zip_code_color(form_page: FormPage, expected_color: str):
    actual_color = form_page.get_color("zip-code")
    assert actual_color == expected_color, \
        f"Ожидали {expected_color}, получили {actual_color}"


@allure.step("Проверка, что поля {fields} подсвечены зелёным")
def check_green_fields_color(
        form_page: FormPage, fields: list[str], expected_color: str):
    for field in fields:
        actual_color = form_page.get_color(field)
        assert actual_color == expected_color, \
            f"Поле {field}: ожидали {expected_color}, получили {actual_color}"


@allure.title("Тест валидации формы")
@allure.description("Проверка подсветки обязательных и "
                    "заполненных полей формы")
@allure.feature("Валидация формы")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_validation(driver):
    red_color = 'rgba(132, 32, 41, 1)'
    green_color = 'rgba(15, 81, 50, 1)'

    form_page = FormPage(driver)

    with allure.step("Открытие страницы формы"):
        form_page.open()

    with allure.step("Заполнение формы корректными данными"):
        form_page.fill_field("first-name", "Иван")
        form_page.fill_field("last-name", "Петров")
        form_page.fill_field("address", "Ленина, 55/3")
        form_page.fill_field("e-mail", "test@skypro.com")
        form_page.fill_field("phone", "+7985899998787")
        form_page.fill_field("city", "Москва")
        form_page.fill_field("country", "Россия")
        form_page.fill_field("job-position", "QA")
        form_page.fill_field("company", "Skypro")

    with allure.step("Отправка формы"):
        form_page.submit()

    # Проверки через @allure.step функции
    check_zip_code_color(form_page, red_color)
    check_green_fields_color(
        form_page,
        ["first-name", "last-name", "address", "e-mail", "phone",
         "city", "country", "job-position", "company"],
        green_color
    )

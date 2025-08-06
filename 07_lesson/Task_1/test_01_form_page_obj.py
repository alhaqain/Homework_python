import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from FormPage import FormPage


@pytest.fixture()
def driver():
    service = EdgeService(executable_path=r"msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    red_color = 'rgba(132, 32, 41, 1)'
    green_color = 'rgba(15, 81, 50, 1)'

    form_page = FormPage(driver)
    form_page.open()

    form_page.fill_field("first-name", "Иван")
    form_page.fill_field("last-name", "Петров")
    form_page.fill_field("address", "Ленина, 55/3")
    form_page.fill_field("e-mail", "test@skypro.com")
    form_page.fill_field("phone", "+7985899998787")
    form_page.fill_field("city", "Москва")
    form_page.fill_field("country", "Россия")
    form_page.fill_field("job-position", "QA")
    form_page.fill_field("company", "Skypro")

    form_page.submit()

    assert form_page.get_color("zip-code") == red_color

    green_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field in green_fields:
        assert form_page.get_color(field) == green_color

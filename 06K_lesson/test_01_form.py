from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_color(driver, field_id):
    return driver.find_element(
        By.CSS_SELECTOR, f'#{field_id}').value_of_css_property("color")


def test_form_validation():
    red_color = 'rgba(132, 32, 41, 1)'
    green_color = 'rgba(15, 81, 50, 1)'

    service = EdgeService(executable_path=r"msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_color = get_color(driver, "zip-code")
    assert zip_color == red_color

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field in fields_to_check:
        color = get_color(driver, field)
        assert color == green_color

    driver.quit()

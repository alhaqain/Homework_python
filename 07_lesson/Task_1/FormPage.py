from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
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

    def open(self):
        self.driver.get(self.url)

    def fill_field(self, field_name, value):
        element = self.driver.find_element(*self.fields[field_name])
        element.clear()
        element.send_keys(value)

    def submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_color(self, field_id):
        return self.driver.find_element(
            By.CSS_SELECTOR, f'#{field_id}').value_of_css_property("color")

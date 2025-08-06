from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = ("https://bonigarcia.dev/"
                    "selenium-webdriver-java/slow-calculator.html")

        self.delay_input = (By.ID, "delay")
        self.result_screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: int):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, label: str):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']")
        button.click()

    def wait_for_result(
            self, expected_result: str, timeout: int = 50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.result_screen, expected_result)
        )

    def get_result(self):
        return self.driver.find_element(*self.result_screen).text

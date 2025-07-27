from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys('45')

    for button in ["7", "+", "8", "="]:
        driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

    driver.quit()

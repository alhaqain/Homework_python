import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
      service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_page_object(driver):
    calc_page = CalcPage(driver)
    calc_page.open()

    calc_page.set_delay(45)

    for btn in ["7", "+", "8", "="]:
        calc_page.click_button(btn)

    calc_page.wait_for_result("15", timeout=50)
    result = calc_page.get_result()

    assert result == "15"

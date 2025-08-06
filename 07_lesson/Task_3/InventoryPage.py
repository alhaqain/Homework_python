from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_id: str):
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()

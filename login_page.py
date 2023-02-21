from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def set_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def get_error_message(self):
        error_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        return error_message.text

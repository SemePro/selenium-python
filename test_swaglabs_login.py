import pytest
from selenium import webdriver
from login_page import LoginPage

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.load()
        login_page.set_username("standard_user")
        login_page.set_password("secret_sauce")
        login_page.click_login_button()

        # Verify successful login
        assert driver.title == "Swag Labs"

    def test_invalid_login(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.load()
        login_page.set_username("invalid_user")
        login_page.set_password("invalid_password")
        login_page.click_login_button()

        # Verify error message
        assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

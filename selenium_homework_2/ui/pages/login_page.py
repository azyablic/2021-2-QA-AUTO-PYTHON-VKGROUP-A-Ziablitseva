from .base_page import BasePage
from selenium_homework_2.ui.locators import LoginPageLocators
from .main_page import MainPage


class LoginPage(BasePage):
    locators = LoginPageLocators
    url = 'https://target.my.com/'

    def login(self, email_value, password_value):
        self.click(self.locators.IN_LOCATOR)
        email = self.find(self.locators.EMAIL_LOCATOR)
        email.send_keys(email_value)
        password = self.find(self.locators.PASSWORD_LOCATOR)
        password.send_keys(password_value)
        self.click(self.locators.ENTER_LOCATOR)
        return MainPage(self.driver)

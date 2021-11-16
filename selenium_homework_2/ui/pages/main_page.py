from .base_page import BasePage
from selenium_homework_2.ui.locators import MainPageLocators


class MainPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = MainPageLocators

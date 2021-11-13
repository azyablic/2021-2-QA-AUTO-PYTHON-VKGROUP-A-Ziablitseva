import allure
from .base import BaseCase
import pytest
import selenium_homework_2.credits as credits
from .ui.locators import LoginPageLocators
from selenium.webdriver.common.by import By


@allure.feature('UI tests')
@pytest.mark.usefixtures('login')
class TestUI(BaseCase):
    @pytest.mark.UI("UI")
    def test_create_campaign(self):
        name = self.campaign_page.create_campaign()
        assert self.base_page.is_element_present((By.XPATH, f"//a[@title='{name}']"))

    @pytest.mark.UI("UI")
    def test_create_segment(self):
        segment_name = self.segments_page.create_segment()
        assert self.base_page.is_element_present((By.XPATH, f"//a[@title='{segment_name}']"))

    @pytest.mark.UI("UI")
    def test_delete_segment(self):
        segment_name = self.segments_page.create_segment()
        self.segments_page.delete_segment(segment_name)
        assert self.base_page.is_element_present((By.XPATH, f"//a[@title='{segment_name}']")) is False


@allure.feature('UI tests')
class TestLogin(BaseCase):
    @pytest.mark.UI("UI")
    @pytest.mark.parametrize(['email', 'password'],
                             [
                                 pytest.param(
                                     credits.email, credits.wrong_password
                                 ),
                                 pytest.param(
                                     credits.wrong_email, credits.password
                                 )
                             ]
                             )
    def test_login_failure(self, email, password):
        self.login_page.login(email, password)
        assert self.base_page.find(LoginPageLocators.EROR_LOCATOR).is_displayed()

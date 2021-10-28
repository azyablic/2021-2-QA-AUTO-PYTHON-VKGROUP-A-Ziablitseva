from .base import BaseCase
from .ui import locators
import pytest
import time
import selenium_homework.credits as credits


class TestOne(BaseCase):
    @pytest.mark.UI("UI")
    def test_login(self):
        BaseCase.login(self)
        time.sleep(5)
        assert 'Кампании' in self.driver.title

    @pytest.mark.UI("UI")
    def test_logout(self):
        BaseCase.login(self)
        time.sleep(5)
        BaseCase.click(self, locators.RIGHT_SIDE_BUTTON)
        time.sleep(5)
        BaseCase.click(self, locators.LOGOUT_BUTTON)
        assert 'Кампании' not in self.driver.title

    @pytest.mark.UI("UI")
    def test_change_contact_info(self):
        BaseCase.login(self)
        BaseCase.wait_before_click(self, locators.PROFILE_BUTTON)
        BaseCase.click(self, locators.PROFILE_BUTTON)
        name = BaseCase.find(self, locators.NAME_LOCATOR).clear()
        name = BaseCase.find(self, locators.NAME_LOCATOR)
        name.send_keys(credits.name)
        phone = BaseCase.find(self, locators.PHONE_LOCATOR).clear()
        phone = BaseCase.find(self, locators.PHONE_LOCATOR)
        phone.send_keys(credits.phone)
        BaseCase.click(self, locators.SUBMIT_BUTTON)
        name = BaseCase.find(self, locators.NAME_LOCATOR)
        assert name.get_attribute('value') == credits.name

    @pytest.mark.UI("UI")
    @pytest.mark.parametrize(['locator', 'title'],
                             [
                                 pytest.param(
                                     locators.BILLING_BUTTON, 'Лицевой счет'
                                 ),
                                 pytest.param(
                                     locators.PRO_BUTTON, 'myTarget Pro'
                                 )
                             ]
                             )
    def test_change_pages(self, locator, title):
        BaseCase.login(self)
        BaseCase.wait_before_click(self, locator)
        BaseCase.click(self, locator)
        assert title in self.driver.title

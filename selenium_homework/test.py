from .base import BaseCase
from .ui import locators
import pytest
import time


class TestOne(BaseCase):
    def test_title(self):
        assert "myTarget" in self.driver.title

    @pytest.mark.UI("UI")
    def test_login(self):
        BaseCase.login(self)
        assert "zyablitseva.an@yandex.ru" in self.driver.page_source

    @pytest.mark.UI("UI")
    def test_logout(self):
        BaseCase.login(self)
        time.sleep(5)
        BaseCase.click(self, locators.RIGHT_SIDE_BUTTON)
        time.sleep(5)
        BaseCase.click(self, locators.LOGOUT_BUTTON)
        assert "zyablitseva.an@yandex.ru" not in self.driver.page_source

    @pytest.mark.UI("UI")
    def test_change_contact_info(self):
        BaseCase.login(self)
        BaseCase.wait_before_click(self, locators.PROFILE_BUTTON)
        BaseCase.click(self, locators.PROFILE_BUTTON)
        name = BaseCase.find(self, locators.NAME_LOCATOR).clear()
        name = BaseCase.find(self, locators.NAME_LOCATOR)
        name.send_keys("qwertyu")
        phone = BaseCase.find(self, locators.PHONE_LOCATOR).clear()
        phone = BaseCase.find(self, locators.PHONE_LOCATOR)
        phone.send_keys("+71111111111")
        BaseCase.click(self, locators.SUBMIT_BUTTON)
        name = BaseCase.find(self, locators.NAME_LOCATOR)
        assert name.get_attribute('value') == 'qwertyu'

    @pytest.mark.UI("UI")
    @pytest.mark.parametrize(['locator', 'url'],
                             [
                                 pytest.param(
                                     locators.BILLING_BUTTON, 'https://target.my.com/billing'
                                 ),
                                 pytest.param(
                                     locators.PRO_BUTTON, 'https://target.my.com/pro'
                                 )
                             ]
                             )
    def test_change_pages(self, locator, url):
        BaseCase.login(self)
        BaseCase.wait_before_click(self, locator)
        BaseCase.click(self, locator)
        assert url == self.driver.current_url

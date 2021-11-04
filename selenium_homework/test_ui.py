from .base import BaseCase
from .ui import locators
import pytest
import selenium_homework.credits as credits


class TestOne(BaseCase):
    @pytest.mark.UI("UI")
    def test_login(self):
        BaseCase.login(self)
        assert BaseCase.find(self, locators.PROFILE_BUTTON).is_displayed()

    @pytest.mark.UI("UI")
    def test_logout(self):
        BaseCase.login(self)
        BaseCase.click(self, locators.RIGHT_SIDE_BUTTON)
        BaseCase.click(self, locators.LOGOUT_BUTTON, 15)
        assert BaseCase.find(self, locators.IN_LOCATOR, 15).is_displayed()

    @pytest.mark.UI("UI")
    def test_change_contact_info(self):
        BaseCase.login(self)
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
    @pytest.mark.parametrize(['locator_to_search', 'locator_to_check'],
                             [
                                 pytest.param(
                                     locators.BILLING_BUTTON, locators.DEPOSIT_LOCATOR
                                 ),
                                 pytest.param(
                                     locators.PRO_BUTTON, locators.PRO_LOGO
                                 )
                             ]
                             )
    def test_change_pages(self, locator_to_search, locator_to_check):
        BaseCase.login(self)
        BaseCase.click(self, locator_to_search)
        assert BaseCase.find(self, locator_to_check).is_displayed()

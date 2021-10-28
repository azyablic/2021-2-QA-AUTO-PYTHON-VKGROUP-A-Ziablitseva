import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import selenium_homework.credits as credits
from .ui import locators

CLICK_RETRY = 10


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_before_click(self, locator):
        return self.wait(15).until(EC.presence_of_element_located(locator))

    def login(self):
        self.click(locators.IN_LOCATOR)
        email = self.find(locators.EMAIL_LOCATOR)
        email.send_keys(credits.email)
        password = self.find(locators.PASSWORD_LOCATOR)
        password.send_keys(credits.password)
        self.click(locators.ENTER_LOCATOR)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

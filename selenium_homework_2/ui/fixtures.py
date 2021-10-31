import pytest

from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.campaign_page import CampaignPage
from .pages.main_page import MainPage
from .pages.segments_page import SegmentsPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)


@pytest.fixture
def segments_page(driver):
    return SegmentsPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

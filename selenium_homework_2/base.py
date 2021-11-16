import pytest
from _pytest.fixtures import FixtureRequest
import selenium_homework_2.credits as credits
from .ui.pages.base_page import BasePage
from .ui.pages.login_page import LoginPage
from .ui.pages.campaign_page import CampaignPage
from .ui.pages.main_page import MainPage
from .ui.pages.segments_page import SegmentsPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.campaign_page: CampaignPage = request.getfixturevalue('campaign_page')
        self.segments_page: SegmentsPage = request.getfixturevalue('segments_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')

    @pytest.fixture
    def login(self):
        return self.login_page.login(credits.email, credits.password)

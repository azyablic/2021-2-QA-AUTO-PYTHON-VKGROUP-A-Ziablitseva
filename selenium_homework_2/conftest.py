from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .ui.fixtures import *


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get("https://target.my.com/")
    yield browser
    browser.quit()

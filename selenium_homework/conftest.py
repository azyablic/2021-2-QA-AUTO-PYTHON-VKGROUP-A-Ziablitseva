import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(executable_path='C:\\Users\Anna Zyabliceva\Downloads\chromedriver_win32\chromedriver')
    browser.maximize_window()
    browser.get("https://target.my.com/")
    yield browser
    browser.close()

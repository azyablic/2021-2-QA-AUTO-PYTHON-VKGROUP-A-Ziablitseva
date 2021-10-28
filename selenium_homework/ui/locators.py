from selenium.webdriver.common.by import By

IN_LOCATOR = (By.XPATH, "//div[contains(@class,'responseHead-module-button')]")
EMAIL_LOCATOR = (By.NAME, "email")
PASSWORD_LOCATOR = (By.NAME, "password")
ENTER_LOCATOR = (By.XPATH, "//div[contains(@class,'authForm-module-button')]")
RIGHT_SIDE_BUTTON = (By.XPATH, "//div[contains(@class,'rightButton')]")
LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выйти']")
PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")
NAME_LOCATOR = (By.XPATH, "//div[@data-name='fio']/child::div[contains(@class, 'input')]/child::input")
PHONE_LOCATOR = (By.XPATH, "//div[@data-name='phone']/child::div[contains(@class, 'input')]/child::input")
SUBMIT_BUTTON = (By.XPATH, "//div[text()='Сохранить']")
BILLING_BUTTON = (By.XPATH, "//a[text()='Баланс']")
PRO_BUTTON = (By.XPATH, "//a[text()='PRO']")

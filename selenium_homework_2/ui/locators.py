from selenium.webdriver.common.by import By


class LoginPageLocators:
    IN_LOCATOR = (By.XPATH, "//div[contains(@class,'responseHead-module-button')]")
    EMAIL_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    ENTER_LOCATOR = (By.XPATH, "//div[contains(@class,'authForm-module-button')]")
    EROR_LOCATOR = (By.XPATH, "//div[contains(@class, 'formMsg')]")


class MainPageLocators:
    RIGHT_SIDE_BUTTON = (By.XPATH, "//div[contains(@class,'rightButton')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
    PROFILE_BUTTON = (By.XPATH, "//a[@href='/profile']")
    BILLING_BUTTON = (By.XPATH, "//a[@href='/billing']")
    PRO_BUTTON = (By.XPATH, "//a[@href='/pro']")
    SEGMENTS_BUTTON = (By.XPATH, "//a[@href='/segments']")


class ProfilePageLocators:
    NAME_LOCATOR = (By.XPATH, "//div[@data-name='fio']/child::div[contains(@class, 'input')]/child::input")
    PHONE_LOCATOR = (By.XPATH, "//div[@data-name='phone']/child::div[contains(@class, 'input')]/child::input")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'button_submit')]")


class CampaignPageLocators:
    CREATE_BUTTON = (By.XPATH, "//div[contains(@class, 'create')]/child::div[contains(@class, 'button')]")
    TRAFFIC_BUTTON = (By.XPATH, "//div[contains(@class,'traffic')]")
    INPUT_URL = (By.XPATH, "//input[contains(@class,'Url')]")
    BANNER_BUTTON = (By.XPATH, "//div[contains(@id, 'banner')]")
    INPUT_IMAGE = (By.XPATH, "//div[contains(@class,'upload')]/child::input[@type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'footer')]/child::button[contains(@class,'button_submit')]")
    INPUT_CAMPAIGN_NAME = (By.XPATH, "//div[contains(@class, 'input_campaign-name')]/child::div/child::input")
    CAMPAIGN_NAME = (By.XPATH, "//a[contains(@class, 'campaignName')]")
    INPUT_URL_AD = (By.XPATH, "//input[contains(@data-name, 'primary')]")


class SegmentsPageLocators:
    SEGMENTS_BUTTON = (By.XPATH, "//a[@href='/segments']")
    CREATE_BUTTON = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_submit')]")
    CHECKBOX = (By.XPATH, "//input[contains(@class, 'checkbox')]")
    INPUT_NAME = (By.XPATH, "//div[contains(@class,'input_create-segment')]//input")
    SEGMENT = (By.XPATH, "//div[contains(@class,'cells-module')]/a[contains(@href,'segments_list')]")
    APPS_AND_GAMES_SEGMENT = (By.XPATH, "//div[@class='adding-segments-item']")
    ACTIONS_BUTTON = (By.XPATH, "//div[contains(@class,'segmentsTable-module-selectItem')]")
    DELETE_BUTTON = (By.XPATH, "//li[contains(@data-id,'remove')]")
    SEGMENTS_COUNT = (By.XPATH, "//span[contains(@class, 'left-nav__count')]")
    ADD_SEGMENT_BUTTON = (By.XPATH, "//div[contains(@class, 'adding')]/button[contains(@class, 'button_submit')]")

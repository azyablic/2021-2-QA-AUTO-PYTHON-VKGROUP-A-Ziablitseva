import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium_homework_2.ui.locators import SegmentsPageLocators
from faker import Faker


class SegmentsPage(BasePage):
    locators = SegmentsPageLocators

    @allure.step('Creating segment')
    def create_segment(self):
        self.click(self.locators.SEGMENTS_BUTTON)
        segments_count = self.find(self.locators.SEGMENTS_COUNT).text
        if int(segments_count) == 0:
            self.click(self.locators.CREATE_BUTTON)
        else:
            self.click(self.locators.SUBMIT_BUTTON)
            self.click(self.locators.APPS_AND_GAMES_SEGMENT)

        self.click(self.locators.CHECKBOX)
        submit_button = self.find(self.locators.ADD_SEGMENT_BUTTON)
        self.scroll_to(submit_button)
        self.click(self.locators.ADD_SEGMENT_BUTTON)
        self.wait()
        name = self.find(self.locators.INPUT_NAME)
        name.clear()
        name = self.find(self.locators.INPUT_NAME)
        segment_name = Faker().first_name()
        name.send_keys(segment_name)
        self.click(self.locators.SUBMIT_BUTTON)
        return segment_name

    @allure.step('Deleting segment')
    def delete_segment(self, segment_name):
        self.click((By.XPATH,
                    f"//a[@title='{segment_name}']/ancestor::div[contains(@class,'main-module-Cell')]/preceding-sibling::div//input"))
        self.click(self.locators.ACTIONS_BUTTON)
        self.click(self.locators.DELETE_BUTTON)

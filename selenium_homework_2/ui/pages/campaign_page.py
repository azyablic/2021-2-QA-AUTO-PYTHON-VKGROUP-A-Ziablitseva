from .base_page import BasePage
from selenium_homework_2.ui.locators import CampaignPageLocators
from faker import Faker
from PIL import Image
import time
import os


class CampaignPage(BasePage):
    locators = CampaignPageLocators

    def create_campaign(self):
        self.click(self.locators.CREATE_BUTTON)
        self.click(self.locators.TRAFFIC_BUTTON)
        url_input = self.find(self.locators.INPUT_URL)
        url = self.get_random_url()
        url_input.send_keys(url)
        banner_button = self.find(self.locators.BANNER_BUTTON)
        self.scroll_to(banner_button)
        self.click(self.locators.BANNER_BUTTON)
        image_input = self.find(self.locators.INPUT_IMAGE)
        self.scroll_to(image_input)
        image_input.send_keys(self.get_random_picture())
        url_ad = self.find(self.locators.INPUT_URL_AD)
        url_ad.send_keys(url)
        campaign_name = self.find(self.locators.INPUT_CAMPAIGN_NAME)
        self.scroll_to(campaign_name)
        campaign_name.clear()
        campaign_name = self.find(self.locators.INPUT_CAMPAIGN_NAME)
        name = self.get_random_name()
        campaign_name.send_keys(name)
        self.click(self.locators.SUBMIT_BUTTON)
        time.sleep(5)
        return name

    def get_random_url(self):
        fake = Faker()
        return fake.domain_name()

    def get_random_name(self):
        fake = Faker()
        return fake.company()

    def get_random_picture(self):
        color = tuple(map(int, Faker().rgb_color().split(',')))
        size = (240, 400)
        img = Image.new('RGB', size, color)
        img_name = Faker().color_name()
        path = os.path.join(
            "C:\\Users\Anna Zyabliceva\PycharmProjects\\2021-2-QA-AUTO-PYTHON-VKGROUP-A-Ziablitseva\selenium_homework_2\\files",
            f"{img_name}.png")
        img.save(path)
        return path

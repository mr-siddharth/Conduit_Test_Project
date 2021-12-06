from pageObjects.basepage import BasePage
from pageObjects.baseelements import *


class LnkSettings(BaseLinkElement):
    locator = (By.CSS_SELECTOR, "a[href='#settings']")


class LnkNewPost(BaseLinkElement):
    locator = (By.CSS_SELECTOR, "a[href='#editor']")


class UserHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.link_settings = LnkSettings(driver)
        self.link_new_post = LnkNewPost(driver)

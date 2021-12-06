from pageObjects.basepage import BasePage
from pageObjects.baseelements import *


class LnkHome(BaseLinkElement):
    locator = (By.XPATH, "//a[text()='Home']")


class LnkSignIn(BaseLinkElement):
    locator = (By.CSS_SELECTOR, "a[href='#login']")


class LnkSignUp(BaseLinkElement):
    locator = (By.CSS_SELECTOR, "a[href='#register']")


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.home_link = LnkHome(driver)
        self.signin_link = LnkSignIn(driver)
        self.signup_link = LnkSignUp(driver)

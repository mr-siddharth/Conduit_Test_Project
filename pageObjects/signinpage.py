from pageObjects.basepage import BasePage
from pageObjects.baseelements import *


class TxtEmail(BaseTxtElement):
    locator = (By.CSS_SELECTOR, "input[type='email']")


class TxtPassword(BaseTxtElement):
    locator = (By.CSS_SELECTOR, "input[type='password']")


class BtnSignIn(BaseButtonElement):
    locator = (By.CSS_SELECTOR, "button[type=submit]")


class ErrorMessages(BaseElement):
    locator = (By.CSS_SELECTOR, ".error-messages")


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.txt_email = TxtEmail(driver)
        self.txt_password = TxtPassword(driver)
        self.btn_signin = BtnSignIn(driver)
        self.error_messages = ErrorMessages(driver)

    def signin(self, email, password):
        self.txt_email.enter(email)
        self.txt_password.enter(password)
        self.btn_signin.click()

    def enter_email(self, email):
        self.txt_email.enter(email)

    def enter_password(self, password):
        self.txt_password.enter(password)

    def click_signin(self):
        self.btn_signin.click()

    def get_error_messages(self):
        return self.error_messages.text()

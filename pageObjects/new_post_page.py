from pageObjects.basepage import BasePage
from pageObjects.baseelements import *


class TxtArticleTitle(BaseTxtElement):
    locator = (By.CSS_SELECTOR, "input[placeholder='Article Title']")


class TxtAbout(BaseTxtElement):
    locator = (By.CSS_SELECTOR, 'input[placeholder="What\'s this article about?"]')


class TxtContent(BaseTxtElement):
    locator = (By.CSS_SELECTOR, "textarea")


class TxtTags(BaseTxtElement):
    locator = (By.CSS_SELECTOR, "input[placeholder='Enter tags']")


class BtnPublish(BaseButtonElement):
    locator = (By.XPATH, "//button[text()='Publish Article']")


class ErrorMessages(BaseElement):
    locator = (By.CSS_SELECTOR, ".error-messages")


class NewPostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.txt_article_title = TxtArticleTitle(driver)
        self.txt_about = TxtAbout(driver)
        self.txt_article_content = TxtContent(driver)
        self.txt_tags = TxtTags(driver)
        self.btn_publish = BtnPublish(driver)
        self.error_messages = ErrorMessages(driver)

    def get_error_messages(self):
        return self.error_messages.text()

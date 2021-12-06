from pageObjects.basepage import BasePage
from pageObjects.baseelements import *
from testLib.lib import wait_till_dom_doesnot_change


class ArticleTitle(BaseElement):
    locator = (By.CSS_SELECTOR, "h1")


class LnkAuthor(BaseLinkElement):
    locator = (By.CSS_SELECTOR, "a.author")


class ArticleCreatedDate(BaseElement):
    locator = (By.CSS_SELECTOR, "span.date")


class ArticleContent(BaseElement):
    locator = (By.CSS_SELECTOR, "div.article-content p")


class ArticlePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.article_title = ArticleTitle(driver)
        self.link_article_author = LnkAuthor(driver)
        self.article_created_date = ArticleCreatedDate(driver)
        self.article_content = ArticleContent(driver)

    def get_article_title(self):
        return self.article_title.text()

    def get_article_author(self):
        return self.link_article_author.text()

    def get_article_content(self):
        return self.article_content.text()

    def get_article_created_date(self):
        return self.article_created_date.text()

    def get_article_id_from_url(self):
        # Wait for few seconds before the id appears in the URL:
        wait_till_dom_doesnot_change(self.driver)
        try:
            return self.get_url().split("/article/")[1].split('?')[0].split('/')[0]
        except IndexError:
            return None

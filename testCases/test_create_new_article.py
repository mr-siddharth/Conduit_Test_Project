import pytest
from pageObjects.signinpage import SignInPage
from pageObjects.homepage import HomePage
from pageObjects.user_homepage import UserHomePage
from pageObjects.new_post_page import NewPostPage
from pageObjects.article_page import ArticlePage
import utilities.readconfig as config
from testLib.lib import get_random_string
from datetime import datetime


@pytest.fixture(scope="module")
def credentials():
    return {
        "email": config.get_test_email(),
        "password": config.get_test_password()
    }


@pytest.mark.usefixtures('credentials')
class TestsCreateArticle:

    @pytest.fixture
    def signin_page(self, driver):
        self.base_url = config.get_base_url()
        self.driver = driver
        self.driver.get(self.base_url)
        HomePage(driver).signin_link.click()
        return SignInPage(self.driver)

    @pytest.fixture
    def new_post_page(self, logger, signin_page, credentials):
        logger.info(f"Attempting login using email: {credentials['email']} and password: {credentials['password']}")
        signin_page.signin(credentials['email'], credentials['password'])
        logger.info("login successful")
        UserHomePage(self.driver).link_new_post.click()
        return NewPostPage(self.driver)

    @pytest.mark.smoke
    def test_create_new_article(self, logger, new_post_page):
        """
        Verifies that a signed-in user can create a new article/post.
        """

        random_string = get_random_string(length=10)
        new_post_page.txt_article_title.enter("Test Article Title " + random_string)
        new_post_page.txt_about.enter("Article About " + random_string)
        new_post_page.txt_article_content.enter(
            "This is an article generated by an automated test. " + random_string)
        new_post_page.btn_publish.click()  # user is navigated to the article details page
        article_page = ArticlePage(self.driver)
        assert article_page.article_title.is_present()
        assert article_page.get_article_id_from_url()


@pytest.mark.usefixtures('credentials')
class TestsVerifyArticleDetails:

    @pytest.fixture(scope='class')
    def signin_page(self, request, driver_class_scoped):
        """
        Navigate to the Sign-In page.
        """
        driver = driver_class_scoped
        request.cls.base_url = config.get_base_url()
        request.cls.driver = driver
        driver.get(self.base_url)
        HomePage(driver).signin_link.click()
        return SignInPage(driver)

    @pytest.fixture(scope='class')
    def new_post_page(self, logger, signin_page, credentials):
        """
        Sign-in and navigate to the New Post page.
        """
        logger.info(f"Attempting login using email: {credentials['email']} and password: {credentials['password']}")
        signin_page.signin(credentials['email'], credentials['password'])
        logger.info("login successful")
        UserHomePage(self.driver).link_new_post.click()
        return NewPostPage(self.driver)

    @pytest.fixture(scope='class')
    def new_article_details(self, logger, new_post_page):
        """
        This fixture creates a new article and returns its details.
        The test cases then verify these details on the article details page.
        """

        random_string = get_random_string(length=10)
        article_details = dict()
        article_details['title'] = "Test Article Title " + random_string
        article_details['about'] = ("Article About " + random_string)
        article_details['content'] = "This is an article generated by an automated test. " + random_string
        article_details['date'] = datetime.now().strftime("%a %b %d %Y")
        article_details['author'] = config.get_test_username()

        new_post_page.txt_article_title.enter(article_details['title'])
        new_post_page.txt_about.enter(article_details['about'])
        new_post_page.txt_article_content.enter(article_details['content'])
        new_post_page.btn_publish.click()
        article_details['url_id'] = ArticlePage(self.driver).get_article_id_from_url()
        logger.info(f"A new article was created. Details: {article_details}")

        return article_details

    @pytest.fixture(scope='class')
    def article_page(self, new_article_details):
        """
        This fixture launches the article details page using the url-id for the
        newly created article.
        """
        self.driver.get(fr"{self.base_url}#/article/{new_article_details['url_id']}/")
        return ArticlePage(self.driver)

    def test_new_article_title(self, new_article_details, article_page):
        """
        Verifies the title of the newly created article on the article details page.
        """
        assert article_page.get_article_title() == new_article_details['title']

    def test_new_article_author(self, new_article_details, article_page):
        """
        Verifies the author (username) of the newly created article on the article details page.
        """
        assert article_page.get_article_author() == new_article_details['author']

    def test_new_article_content(self, new_article_details, article_page):
        """
        Verifies the content of the newly created article on the article details page.
        """
        assert article_page.get_article_content() == new_article_details['content']

    def test_new_article_date(self, new_article_details, article_page):
        """
        Verifies the creation date of the newly created article on the article details page.
        """
        assert article_page.get_article_created_date() == new_article_details['date']

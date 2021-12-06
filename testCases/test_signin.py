import pytest
from pageObjects.signinpage import SignInPage
from pageObjects.homepage import HomePage
from pageObjects.user_homepage import UserHomePage
import utilities.readconfig as config


@pytest.fixture(scope="module")
def credentials():
    return {
        "email": config.get_test_email(),
        "password": config.get_test_password()
    }


@pytest.mark.usefixtures('credentials')
class TestsLogIn:

    @pytest.fixture
    def signin_page(self, driver):
        self.base_url = config.get_base_url()
        self.driver = driver
        self.driver.get(self.base_url)
        HomePage(driver).signin_link.click()
        return SignInPage(self.driver)

    @pytest.mark.smoke
    def test_signin_valid_credentials(self, logger, signin_page, credentials):
        """Verifies that user is able to login with valid credentials."""

        logger.info(f"Attempting login using email: {credentials['email']} and password: {credentials['password']}")
        signin_page.signin(credentials['email'], credentials['password'])
        assert UserHomePage(self.driver).link_settings.is_present()
        logger.info("login successful")

    @pytest.mark.smoke
    def test_signin_invalid_password(self, logger, signin_page, credentials):
        """Verifies that user is NOT able to login with invalid password."""

        sp = SignInPage(self.driver)
        logger.info(f"Attempting login using email: {credentials['email']} and password: {'invalid_pswd'}")
        sp.signin(credentials['email'], 'invalid_pswd')
        assert sp.error_messages.is_present()
        logger.info("login failed as expected")

    def test_signin_invalid_password_verify_error_message(self, logger, signin_page, credentials):
        """
        Verifies that the following message is displayed when the user
        tries to login with invalid password.
        Expected Error Message: "email or password is invalid"
        """
        sp = SignInPage(self.driver)
        logger.info(f"Attempting login using email: {credentials['email']} and password: {'invalid_pswd'}")
        sp.signin(credentials['email'], 'invalid_pswd')
        assert sp.get_error_messages() == "email or password is invalid"
        logger.info("login failed as expected")

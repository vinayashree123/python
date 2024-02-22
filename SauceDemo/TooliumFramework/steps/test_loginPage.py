import unittest
from behave import given, when, then
from base.BasePage import BaseClass
from pages.loginPage import LoginPage

class LoginPageTest(unittest.TestCase):

    @given('create class objects')
    def create_class_objects(self):
        # Assuming you have a WebDriver setup fixture (e.g., setup_webdriver) that provides 'self.driver'
        # If not, make sure to initialize 'self.driver' before calling this method
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)

    @when('the user logs in with username "standard_user" and password "secret_sauce"')
    def enter_username_and_password(self):
        self.lp.userDetails()
        self.lp.passwordDetails()

    @then('login successful')
    def test_login_page(self):
        self.lp.clickOnLoginButton()
        # Add assertions or verifications for successful login if needed
        assert self.lp.isLoginSuccessful(), "Login was not successful"

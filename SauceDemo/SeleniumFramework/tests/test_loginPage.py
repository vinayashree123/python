import unittest
import pytest
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.loginPage import LoginPage


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class LoginPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_loginPage(self):
       self.lp.testLoginPage()
    #
    # @pytest.mark.run(order=1)
    # def test_invalid_loginPage(self):
    #     self.lp.enterInvalidUsername()
    #     self.lp.enterInvalidPassword()
    #     self.lp.clickOnLoginButton()

    # @pytest.mark.run(order=1)
    # def test_loginPage(self):
    #     # Enter invalid username and password
    #     self.lp.enterInvalidUsername()
    #     self.lp.enterInvalidPassword()
    #     self.lp.clickOnLoginButton()
    #
    #     # Check if login failed
    #     if self.lp.isLoginFailed():
    #         # Take some action when login fails
    #         print("Login failed. Handling the failure scenario.")
    #         # You can perform additional actions or assertions here
    #     else:
    #         # Continue with the regular flow when login succeeds
    #         print("Login succeeded. Continuing with the regular flow.")
    #         self.lp.userDetails()
    #         self.lp.passwordDetails()
    #         self.lp.clickOnLoginButton()



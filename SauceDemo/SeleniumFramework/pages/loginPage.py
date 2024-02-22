from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl


class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators values in Login Page
    _userName = 'user-name'  # id
    _password = 'password'  # id
    _loginButton = 'login-button'  # id
    _validUsername = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user'
                                                                          'error_user', 'visual_user']
    _validPassword = 'secret_sauce'
    _inValidUsername = 'vina@1234'
    _invalidPassword = '12345'

    def testLoginPage(self):
        self.userDetails()
        self.passwordDetails()
        self.clickOnLoginButton()
        cl.allureLogs("Login Successful")

    def clickOnUserName(self):
        self.clickOnElement(self._userName, 'id')

    def enterValidUsername(self):
        self.sendText(self._validUsername[0], self._userName, 'id')

    def clickOnpPassword(self):
        self.clickOnElement(self._password, 'id')

    def enterValidPassword(self):
        self.sendText(self._validPassword, self._password, 'id')


    def userDetails(self):
        self.clickOnElement(self._userName, 'id')
        self.sendText(self._validUsername[0], self._userName, 'id')

    def passwordDetails(self):
        self.clickOnElement(self._password, 'id')
        self.sendText(self._validPassword, self._password, 'id')

    def clickOnLoginButton(self):
        self.clickOnElement(self._loginButton, 'id')

    def enterInvalidUsername(self):
        self.sendText(self._inValidUsername, self._userName, 'id')

    def enterInvalidPassword(self):
        self.sendText(self._invalidPassword, self._password, 'id')

    def isLoginFailed(self):
        try:
            error_message_element = self.waitForElement('error-message', 'class')
            return "Invalid username or password" in error_message_element.text
        except:
            return False


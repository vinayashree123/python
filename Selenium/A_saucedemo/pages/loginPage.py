from A_saucedemo.base.BasePage import BaseClass


class LoginPageClass(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Login Page
    _userName = 'user-name'  # id
    _password = 'password'  # id
    _loginButton = 'login-button'  # id
    _validUsername = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user'
                                                                          'error_user', 'visual_user']
    _validPassword = 'secret_sauce'

    def clickOnUserName(self):
        self.clickOnElement(self._userName,'id')

    def enterUserName(self):
        self.sendText(self._validUsername[0],self._userName,'id')

    def clickOnPassword(self):
        self.clickOnElement(self._password,'id')

    def enterPassword(self):
        self.sendText(self._validPassword,self._password,'id')

    def clickOnLoginButton(self):
        self.clickOnElement(self._loginButton,'id')

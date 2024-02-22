from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Toolium.base.BasePage import BaseClass

class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators values in Login Page
    _userName = 'user-name'  # id
    _password = 'password'  # id
    _loginButton = 'login-button'  # id
    _successElement = 'success-element-id'  # id

    _validUsername = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user',
                      'error_user', 'visual_user']
    _validPassword = 'secret_sauce'
    _inValidUsername = 'vina@1234'
    _invalidPassword = '12345'

    def userDetails(self):
        self.clickOnElement(self._userName, 'id')
        self.sendText(self._validUsername[0], self._userName, 'id')

    def passwordDetails(self):
        self.clickOnElement(self._password, 'id')
        self.sendText(self._validPassword, self._password, 'id')

    def clickOnLoginButton(self):
        self.clickOnElement(self._loginButton, 'id')

    def isLoginSuccessful(self):
        try:
            # Assuming there is some element that indicates a successful login
            success_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self._successElement))
            )
            return success_element.is_displayed()
        except:
            return False

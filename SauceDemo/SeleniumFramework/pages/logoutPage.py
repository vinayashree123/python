from SeleniumFramework.base.BasePage import BaseClass


class LogoutPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators values in Login Page
    _reactBurgerMenu = 'react-burger-menu-btn'  # id
    _logoutButton = 'logout_sidebar_link'  # id
    _loginButton = 'login-button'  # id

    def clickOnReactBurgerMenu(self):
        self.clickOnElement(self._reactBurgerMenu, 'id')

    def clickOnLogoutButton(self):
        self.clickOnElement(self._logoutButton, 'id')

    def assertIsElementDisplay(self):
        self.isElementDisplayed(self._loginButton, 'id')

import time
import unittest
import pytest
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.loginPage import LoginPage
from SeleniumFramework.pages.logoutPage import LogoutPage
from SeleniumFramework.tests.test_loginPage import LoginPageTest


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class LogoutPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPage(self.driver)
        self.lo = LogoutPage(self.driver)
        self.bp = BaseClass(self.driver)
        # self.tlp = LoginPageTest(self.driver)

    @pytest.mark.run(order=2)
    def test_logoutPage(self):
        try:
            self.lp.testLoginPage()
            self.lo.clickOnReactBurgerMenu()
            time.sleep(3)
            self.lo.clickOnLogoutButton()
            time.sleep(3)
            print('logout successfully')
        except:
            assert self.lo.assertIsElementDisplay(), "User is not redirected to the login page after logout."
            time.sleep(1)

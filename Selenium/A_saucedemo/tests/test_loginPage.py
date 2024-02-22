import unittest
import pytest
from A_saucedemo.pages.loginPage import LoginPageClass

import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Check if the correct directory is in the path
print(sys.path)

from A_saucedemo.base.BasePage import BaseClass

# Your fixtures or other configurations...



@pytest.mark.usefixtures('beforeClas', 'beforeMethod')
class loginPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPageClass(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_loginPage(self):
        self.lp.clickOnUserName()
        self.lp.enterUserName()
        self.lp.clickOnPassword()
        self.lp.enterPassword()
        self.lp.clickOnLoginButton()

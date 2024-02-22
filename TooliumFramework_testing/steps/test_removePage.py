import time
import unittest
import pytest
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.loginPage import LoginPage
from SeleniumFramework.pages.addToCartPge import AddToCartPage
from SeleniumFramework.pages.removePage import RemovePage


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class RemovePageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)
        self.ac = AddToCartPage(self.driver)
        self.rp = RemovePage(self.driver)

    @pytest.mark.run(order=2)
    def test_filter(self):
        self.lp.testLoginPage()
        self.rp.selectFilterByDropDown()
        time.sleep(1)
        self.rp.clickOnProduct()
        self.rp.clickOnAddToCartButton1()
        self.rp.clickOnShoppingCartLink()
        time.sleep(3)

    @pytest.mark.run(order=2)
    def test_removePage(self):
        self.rp.clickOnRemoveButton()
        time.sleep(3)









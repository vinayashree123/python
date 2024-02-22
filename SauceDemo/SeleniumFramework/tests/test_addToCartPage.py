import time
import unittest
import pytest
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.loginPage import LoginPage
from SeleniumFramework.pages.addToCartPge import AddToCartPage


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class AddToCartPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)
        self.ac = AddToCartPage(self.driver)

    @pytest.mark.run(order=1)
    def test_addToCartPage(self):
        self.lp.testLoginPage()
        self.ac.scrollElement()
        time.sleep(4)
        self.ac.clickOnProductAddToCart()
        time.sleep(4)
        self.ac.clickOnAddToCartButton()
        time.sleep(4)
        self.ac.clickOnShoppingCartLink()










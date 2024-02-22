import time
import unittest
import pytest
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.loginPage import LoginPage
from SeleniumFramework.pages.addToCartPge import AddToCartPage
from SeleniumFramework.pages.checkoutPage import CheckoutPage


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class CheckoutPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)
        self.ac = AddToCartPage(self.driver)
        self.co = CheckoutPage(self.driver)

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

    @pytest.mark.run(order=2)
    def test_checkoutPage(self):
        self.co.clickOnCheckoutButton()
        self.co.giveCheckoutInfo()
        self.co.clickOnContinueToCheckout()
        time.sleep(3)
        self.co.clickOnFinishButton()

import time
import unittest
import pytest
from base.BasePage import BaseClass
from pages.loginPage import LoginPage
from pages.addToCartPge import AddToCartPage
from pages.filterPage import FilterPage


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class FilterPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = LoginPage(self.driver)
        self.bp = BaseClass(self.driver)
        self.ac = AddToCartPage(self.driver)
        self.fp = FilterPage(self.driver)

    @pytest.mark.run(order=1)
    def test_filter(self):
        self.lp.testLoginPage()
        self.fp.selectFilterByDropDownUsingOptionValue()
        time.sleep(3)
        self.fp.selectFilterByDropDownUsingOptionIndex()
        time.sleep(3)
        self.fp.selectFilterByDropDownUsingOptionText()
        time.sleep(3)












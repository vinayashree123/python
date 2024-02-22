# import the files
import unittest
from SeleniumFramework.tests.test_loginPage import LoginPageTest
from SeleniumFramework.tests.test_filterPage import FilterPageTest
from SeleniumFramework.tests.test_addToCartPage import AddToCartPageTest
from SeleniumFramework.tests.test_checkoutPage import CheckoutPageTest
from SeleniumFramework.tests.test_removePage import RemovePageTest
from SeleniumFramework.tests.test_logoutPage import LogoutPageTest

# Create the object of the class using unitTest
a = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
b = unittest.TestLoader().loadTestsFromTestCase(FilterPageTest)
c = unittest.TestLoader().loadTestsFromTestCase(AddToCartPageTest)
d = unittest.TestLoader().loadTestsFromTestCase(CheckoutPageTest)
e = unittest.TestLoader().loadTestsFromTestCase(RemovePageTest)
f = unittest.TestLoader().loadTestsFromTestCase(LogoutPageTest)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([a, b, c, d, e, f])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

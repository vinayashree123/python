import time

import pytest
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.base.DriverClass import WebDriverClass


@pytest.fixture(scope='class')
def beforeClass(request):
    print('before class')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver('edge')
    bp = BaseClass(driver)
    bp.launchWebPage("https://www.saucedemo.com/", "Swag Labs")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(2)
    driver.quit()


@pytest.fixture()
def beforeMethod():
    print('before method')
    yield
    print('after method')

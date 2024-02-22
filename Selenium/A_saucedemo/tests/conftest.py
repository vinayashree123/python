import pytest
from A_saucedemo.base.BasePage import BaseClass
from A_saucedemo.base.DriverClass import WebDriverClass

@pytest.fixture(scope='class')
def beforeClass(request):
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver('Edge')
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/", "Selenium Template")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture()
def beforeMethod():
    yield

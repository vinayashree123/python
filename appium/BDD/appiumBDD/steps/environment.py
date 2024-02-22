import time
import pytest
from BDD.appiumBDD.base.Driverclass import Driver

def before_all(context,request):
    print("before class")
    d1 = Driver()
    context.driver = d1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = context.driver
    yield context.driver
    time.sleep(5)
    context.driver.quit()
    print('After Class')

# @pytest.fixture()
# def beforeMethod():
#     print('Before Method')
#     yield
#     print('After Method')

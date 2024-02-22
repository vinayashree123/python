import time
import pytest
from Toolium.base.BasePage import BaseClass
from Toolium.base.DriverClass import WebDriverClass

# Fixture for setting up the WebDriver
@pytest.fixture(scope='class')
def setup_webdriver(request, context):
    print('Setting up WebDriver before class')

    # Initialize WebDriverClass
    context.driver1 = WebDriverClass()

    # Get WebDriver instance for 'edge'
    context.driver = context.driver1.getWebDriver('edge')

    # Initialize BaseClass with the WebDriver
    bp = BaseClass(context.driver)

    # Launch the web page
    bp.launchWebPage("https://www.saucedemo.com/", "Swag Labs")

    # If the request is for a class, set the driver attribute in the request
    if request.cls is not None:
        request.cls.driver = context.driver

    # Yield the WebDriver instance to the tests in the class
    yield context.driver

    # Optional: Add a wait or synchronization mechanism instead of sleep
    time.sleep(2)

    # Quit the WebDriver after the tests in the class
    context.driver.quit()

# If you want to have an after-all cleanup fixture, you can uncomment the code below
# Fixture for cleanup after all tests in the module
# Note: The code is commented out since it's not clear what cleanup is needed
# Uncomment and modify according to your requirements
'''
@pytest.fixture()
def after_all():
    print('Cleaning up after all tests in the module')
    yield
    print('After all cleanup')
'''

# Example usage in a test class
class TestMyWebPage:
    def test_example(self, setup_webdriver):
        # Use the WebDriver instance provided by the fixture
        driver = setup_webdriver
        # Your test code here

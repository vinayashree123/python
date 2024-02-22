import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '13',
                'deviceName': 'f1dd3b4c', 'app': r'C:\Users\vnaganur\Downloads\Android_Demo_App.apk',
                'appPackage': 'com.code2lead.wad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

"""This is the URL of the remote WebDriver server. In this case, you are trying to connect 
to a Selenium server running on the local machine at IP address 127.0.0.1 (localhost)
 and port 4723. The "/wd/hub" path is a common endpoint for WebDriver communication."""

ele_id = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(1)")
ele_id.click()
time.sleep(3)
# ele=driver.driver.find_element(AppiumBy.IMAGE)
ele_cls = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_cls.send_keys("Vinaya")

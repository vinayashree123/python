import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def deviceDriver(deviceid, sysport):
    desired_caps = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'platformVersion': '10',
        'deviceName': 'ZF6224GFW3',
        'app': r'C:\Users\vnaganur\Downloads\Android_Demo_App.apk',
        'appPackage': 'com.code2lead.kwad',
        'appActivity': 'com.code2lead.kwad.MainActivity',
        'udId': deviceid,  # Remove the quotation marks
        'systemPort': sysport,  # Remove the quotation marks
    }

    driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)
    return driver

def enterText(driver):
    ele_id = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(1)")
    ele_id.click()
    time.sleep(3)
    ele_cls = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    ele_cls.send_keys("Vinaya")
    driver.quit()

def test_parallel():
    d1 = deviceDriver('HT73P0200721', 8200)
    enterText(d1)

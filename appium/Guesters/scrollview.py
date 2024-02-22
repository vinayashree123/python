import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'ZF6224GFW3', 'app': r'C:\Users\vnaganur\Downloads\Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele_id = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ScrollView"))
ele_id.click()
ele_id = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
ele_id.click()
time.sleep(2)
driver.quit()

ele = wait.until(lambda x : x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,))


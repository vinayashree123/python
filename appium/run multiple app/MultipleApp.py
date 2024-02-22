import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'ZF6224GFW3', 'app': r'C:\Users\vnaganur\Downloads\Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)

time.sleep(5)
driver.start_activity('com.google.android.gm','com.google.android.gm.ConversationListActivityGmail')

time.sleep(5)

driver.start_activity('com.code2lead.kwad','com.code2lead.kwad.MainActivity')

driver.quit()

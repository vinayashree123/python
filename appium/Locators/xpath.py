import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'ZF6224GFW3', 'app': r'C:\Users\vnaganur\Downloads\Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)


# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]') #xpath and content
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]') #xpath and resource_id
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]') #xpath and text
ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button') #xpath and class
ele_xpath.click()
time.sleep(2)
ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText') #xpath and class
ele_xpath.send_keys("helllo")
driver.quit()


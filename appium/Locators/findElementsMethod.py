import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'platformName': 'Android', 'automationName': 'UiAutomator2', 'platformVersion': '10',
                'deviceName': 'ZF6224GFW3', 'app': r'C:\Users\vnaganur\Downloads\Android_Demo_App.apk',
                'appPackage': 'com.code2lead.kwad', 'appActivity': 'com.code2lead.kwad.MainActivity'}

driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)


element = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Button")
for x in element:
    print(x.text)
for x in element:
    button = x.text
    if button == 'TAB ACTIVITY':
        x.click()
        break
time.sleep(2)
driver.quit()



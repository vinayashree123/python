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

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele_id = wait.until(lambda x: x.find_element(AppiumBy.ID,'com.code2lead.kwad:id/TabView'))
ele_id.click()
print("width and helight",driver.get_window_size())
devicesize = driver.get_window_size()
screenwidth = devicesize['width']
screenheight = devicesize['height']

#right to left here y will half of the height
startx = screenwidth*8/9
endx = screenheight/9
starty = screenwidth/2
endy = screenheight/2

startx1 = screenwidth/8
endx1 = screenheight*8/9
starty1 = screenwidth/2
endy1 = screenheight/2


action = TouchAction(driver)
action.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
time.sleep(2)
# action.long_press(None,startx1,starty1).move_to(None,endx1,endy1).release().perform()
driver.quit()








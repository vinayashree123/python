from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

des_caps = {'platformName' : 'Android','automationName':'UiAutomator2'}
driver = webdriver.Remote('https://127.0.1/wd/hub',des_caps)



#locator
#id , name, classname,xpath
ele = driver.find_element(AppiumBy.ID,'')
ele = driver.find_element(AppiumBy.NAME)

#text,index,content
ele = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().text('')')
ele = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().index(3)')
ele = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description('')')

#guestures
scroll = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).ScrollIntoView(text('')))')

wait = WebDriverWait(20,driver,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException])
ele = wait.until(lambda x: x.find_element(AppiumBy.ID,''))
ele.click()

#tap
action = ActionChains(driver)
action.tap(ele,x,y,2)
action.perform()

#longclick
action.click_and_hold(ele)


#ac
action.scroll_to_element()


#drag and drop
action.click_and_hold(ele).perform()
action.release(ele)


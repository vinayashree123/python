import time

from appiumFramework.utilities.CustomLogger import customLogger
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.log = customLogger()

    def WaitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % locatorvalue))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locatorvalue))
            return element
        else:
            self.log.info("Locator Value " + locatorvalue + " Not found")
        return element

    def getElement(self, locatorvalue, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.WaitForElement(locatorvalue, locatorType)
            self.log.info("Element found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType)
        except:
            self.log.error("Element not found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType)

        return element

    def clickElement(self, locatorvalue, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.WaitForElement(locatorvalue, locatorType)
            element.click()
            self.log.info("Clicked the Element found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType)
        except Exception as e:
            self.log.error("Unable to click Element not found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType)
            self.log.exception(e)
    def sendText(self,text, locatorvalue, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.WaitForElement(locatorvalue, locatorType)
            element.send_keys(text)
            self.log.info("text send on the Element found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType)
        except Exception as e:
            self.log.error("Unable to send text becz Element not found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType)
            self.log.exception(e)
    def isDisplayed(self,locatorvalue, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.WaitForElement(locatorvalue, locatorType)
            element.is_displayed()
            self.log.info(" Element found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType+ "is displayed")
            return True
        except Exception:
            self.log.info("Unable to send text becz Element not found with Locatorvalue " + locatorvalue + " and with locatorType " + locatorType+ "is not displayed")
            return False
    def screenshots(self, screenshotName):
        filename = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotpath = screenshotDirectory + filename
        try:
            self.driver.save_screenshot(screenshotpath)
            self.log.info("Screenshot saved: %s", screenshotpath)
        except Exception as e:
            self.log.error("Failed to save screenshots: %s", str(e))



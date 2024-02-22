from traceback import print_stack

import allure
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import Toolium.utilities.CustomLogger as cl


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Web Page Launched with URL : " + url)
        except:
            self.log.info("Web Page not Launched with URL : " + url)

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type : " + locatorType + " entered is not found")
        return False

    def getWebElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorByType)
        except:
            self.log.error(
                "WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
        return webElement

    def waitForElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
        return webElement

    def clickOnElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info(
                "Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            raise AssertionError(f"Unable to Click on WebElement with locator value {locatorValue} using locatorType {locatorType}")

    def sendText(self, text, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info(
                "Sent the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to Sent the text " + text + " in WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)

    def getText(self, locatorValue, locatorType="id"):
        elementText = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementText = webElement.text
            self.log.info(
                "Got the text " + elementText + " from WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to get the text " + elementText + " from WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()

        return elementText

    def isElementDisplayed(self, locatorValue, locatorType="id"):
        elementDisplayed = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementDisplayed = webElement.is_displayed()
            self.log.info(
                "WebElement is Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "WebElement is not Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()

        return elementDisplayed

    def scrollTo(self, locatorValue, locatorType="id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(
                "Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to scroll to WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()

    def select_option_in_dropdown(self, locatorValue, locatorType="id", optionValue=None, optionIndex=None,optionText=None):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            dropdown = Select(webElement)

            if optionValue is not None:
                dropdown.select_by_value(optionValue)
            elif optionIndex is not None:
                dropdown.select_by_index(optionIndex)
            elif optionText is not None:
                dropdown.select_by_visible_text(optionText)
            else:
                raise ValueError("Either optionValue,optionIndex or optionText must be provided.")

        except Exception as e:
            self.log.error(f"An error occurred while selecting option in dropdown: {e}")
            print_stack()

    def takeScreenshot(self,text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text,attachment_type=AttachmentType.PNG)




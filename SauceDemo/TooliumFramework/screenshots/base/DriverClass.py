from selenium import webdriver
import Toolium.utilities.CustomLogger as cl


class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "edge":
            driver = webdriver.Edge()
            self.log.info("edge is initializing")
        elif browserName == "firefox":
            driver = webdriver.Firefox()
            self.log.info("FireFox Driver is initializing")
        return driver

import time

from selenium import webdriver
from base.DriverClass import WebDriverClass
from base.BasePage_2 import BaseClass

wd = WebDriverClass()
driver = wd.getWebDriver('edge')

bp = BaseClass(driver)
bp.launchWebPage('http://www.dummypoint.com','General Dashboard — DummyPoint')

ele = bp.getWebElement('//*[@id="app"]/div/nav/form/div/input','xpath')
ele.send_keys('vina')
time.sleep(4)

# driver.get('https://www.google.com')
driver.quit()

import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')

assert 'Selenium Template — DummyPoint' in driver.title

driver.minimize_window()
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.quit()

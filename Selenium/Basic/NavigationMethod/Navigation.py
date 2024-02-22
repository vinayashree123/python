import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()
driver.get('http://dummypoint.com/seleniumtemplate.html')
time.sleep(2)

driver.get("http://www.dummypoint.com/Form.html")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

driver.quit()

import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')

ele = driver.find_element(By.ID,'user_input')

ele_d = ele.is_displayed()
print('is displayed',ele_d)

ele_e = ele.is_enabled()
print('is enabled', ele_e)

ele_l = ele.location
print('location is ',ele_l)

ele_s = ele.size
print('size is ',ele_s)

ele.send_keys('vinaya')

ele_a = ele.get_attribute('value')
print('text from edit box',ele_a)



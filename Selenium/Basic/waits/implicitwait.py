import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')

ele = driver.find_elements(By.ID,'menu')

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

driver.implicitly_wait(10)
ele = driver.find_element(By.ID,'user_input')
ele.send_keys('automation')
#
# ele = wait.until(ec.presence_of_element_located((By.ID,'user_input')))
# ele.send_keys('code2leads')
#
time.sleep(3)
driver.quit()

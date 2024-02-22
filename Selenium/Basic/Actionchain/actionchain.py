import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')


# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

ele = wait.until(ec.presence_of_element_located((By.CLASS_NAME,'form-control')))

#create obj for actionchain
options = ActionChains(driver)

#double click action
# options.double_click(ele).perform()
# time.sleep(2)

#right click option
options.context_click(ele).perform()
time.sleep(2)

driver.quit()

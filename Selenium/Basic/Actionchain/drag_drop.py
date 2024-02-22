import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
driver = webdriver.Edge()

driver.get('http://dummypoint.com/DragAndDrop.html')


# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

ele = wait.until(ec.presence_of_element_located((By.ID,'drag')))
ele1 = wait.until(ec.presence_of_element_located((By.ID,'drop')))

#create obj for actionchain
options = ActionChains(driver)

#drag and drop
options.click_and_hold(ele).perform()
options.release(ele1)
time.sleep(5)


driver.quit()

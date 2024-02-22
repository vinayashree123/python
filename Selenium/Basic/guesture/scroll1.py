import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get("https://www.saucedemo.com/")


wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

wait.until(ec.presence_of_element_located((By.ID,'user-name'))).send_keys('standard_user')
wait.until(ec.presence_of_element_located((By.ID,'password'))).send_keys('secret_sauce')
wait.until(ec.presence_of_element_located((By.ID,'login-button'))).click()


scroll_ele = wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="item_3_title_link"]/div')))
action = ActionChains(driver)
action.move_to_element(scroll_ele).perform()
scroll_ele.click()
time.sleep(5)
driver.quit()

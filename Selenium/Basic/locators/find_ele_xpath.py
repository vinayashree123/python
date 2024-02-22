import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')

driver.find_element(By.XPATH,'//*[@id="user_input"]').send_keys('sent by usimg relative xpath')


driver.find_element(By.XPATH,'//*[@id="app"]//input[3]').click()
time.sleep(3)
driver.quit()

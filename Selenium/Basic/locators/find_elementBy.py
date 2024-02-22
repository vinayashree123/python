import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')


#by id
# driver.find_element(By.ID,'user_input').send_keys('vinaya')

#by class
# driver.find_element(By.CLASS_NAME,'entertext').send_keys('class2')

#by_name
# driver.find_element(By.NAME,'textbox').send_keys('by_name')

#by_tag_name
# driver.find_element(By.TAG_NAME,'input').send_keys('by_tag')

#by link
# driver.find_element(By.LINK_TEXT,"Form").click()


driver.find_element(By.PARTIAL_LINK_TEXT,"For").click()
time.sleep(3)
driver.quit()

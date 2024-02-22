import time
from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()
driver.get('http://dummypoint.com/Frame.html')

# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

ele = driver.find_elements(By.TAG_NAME,'iframe')

print('list frame in page',len(ele))

#switch to iframe by index
# time.sleep(2)
# driver.switch_to.frame(1)
#
# data = driver.find_element(By.ID,"framename")
# print("frame name is",data.text)

#switch to iframe by name
# time.sleep(2)
# driver.switch_to.frame('farme1')
#
# data = driver.find_element(By.ID,"framename")
# print('frame name is ',data.text)

# try:
#     driver.switch_to.frame('farme1')
#     data = driver.find_element(By.ID, "framename")
#     print('Frame name inside iframe "frame1" is:', data.text)
# except NoSuchElementException:
#     print('Element not found inside iframe "frame1"')

#switch to iframe by id
# time.sleep(2)
# driver.switch_to.frame('f3')
#
# data = driver.find_element(By.ID,"framename")
# print('frame name is ',data.text)

#switch to iframe by webelemt
# time.sleep(2)
# ele = driver.find_element(By.ID,"f3")
# driver.switch_to.frame(ele)
#
# data = driver.find_element(By.ID,"framename")
# print('frame name is ',data.text)

# Switch to iframe by WebElement
time.sleep(2)
iframe_element = driver.find_element(By.ID, "f2")
driver.switch_to.frame(iframe_element)
#
# # Find the element inside the iframe by ID
# try:
#     data = driver.find_element(By.ID, "framename")
#     print('Frame name inside iframe is:', data.text)
# except NoSuchElementException:
#     print('Element not found inside the iframe')
#
# # Switch back to the main content
# driver.switch_to.default_content()

driver.quit()

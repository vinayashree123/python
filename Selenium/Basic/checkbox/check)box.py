
import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')


# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

c_ele = driver.find_elements(By.NAME,'checkbox')

for checkbox in c_ele:
    check_box = checkbox.get_attribute('value')
    if check_box == 'c2':
        checkbox.click()
        print('is selected',checkbox.is_selected())
        time.sleep(4)


driver.quit()

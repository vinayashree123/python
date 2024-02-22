import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')


# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

r_ele = driver.find_elements(By.NAME,'radio')

for rbutton in r_ele:
    rbutton1 = rbutton.get_attribute('value')
    if rbutton1 == 'Button2':
        rbutton.click()
        print('is selected',rbutton.is_selected())
        time.sleep(4)
        break


driver.quit()

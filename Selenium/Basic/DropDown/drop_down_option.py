import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')


# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

ele = wait.until(ec.presence_of_element_located((By.ID,'dropdown')))

#import select
from selenium.webdriver.support.select import Select

#create obj for select
dd_options = Select(ele)

#list the value of dd
dd_v = dd_options.options

for dd_values in dd_v:
    print(dd_values.text)

#click by index
dd_options.select_by_index(3)
time.sleep(2)

#click by value
dd_options.select_by_value('OptionTWo')
time.sleep(2)

#click by visible text
dd_options.select_by_visible_text('Option4')
time.sleep(2)

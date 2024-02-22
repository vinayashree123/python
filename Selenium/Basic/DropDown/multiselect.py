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

ele = wait.until(ec.presence_of_element_located((By.ID,'multiselect')))

#import select
from selenium.webdriver.support.select import Select

#create obj for select
ms_options = Select(ele)

print('is multisect option is present',ms_options.is_multiple)

#list the value of dd
ms_v = ms_options.options

for ms_values in ms_v:
    print(ms_values.text)

#click by index
ms_options.select_by_index(1)
time.sleep(2)

#click by value
ms_options.select_by_value('mOptionTWo')
time.sleep(2)

#click by visible text
ms_options.select_by_visible_text('mOption3')
time.sleep(2)

#deselect by value
ms_options.deselect_by_value('mOptionTWo')
time.sleep(2)

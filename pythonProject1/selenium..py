import time
from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Edge()

# driver.get('http://dummypoint.com/seleniumtemplate.html')

# driver.find_element(By.ID, 'user_input').send_keys('vinaya')
#
# r_ele = driver.find_elements(By.NAME,'radio')

# for radio in r_ele:
#     r = radio.get_attribute('value')
#     if r == 'Button2':
#         radio.click()
#         time.sleep(3)
#         break
#
# c_ele = driver.find_elements(By.NAME,'checkbox')
#
# for checkbox in c_ele:
#     checkbox2 = checkbox.get_attribute('value')
#     if checkbox2 == 'c2':
#         checkbox.click()
#         time.sleep(3)
#         break
#
#
#
# # ele_scroll = driver.find_element(By.ID,'submitbutton')
#
# dd_ele = driver.find_element(By.CSS_SELECTOR,'#dropdown')
#
# action = ActionChains(driver)
# action.click_and_hold(dd_ele).perform()
# time.sleep(3)
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

# dd_ele = driver.find_element(By.CSS_SELECTOR,'#dropdown')
# # dd_ele = wait.until(ec.presence_of_element_located(By.CSS_SELECTOR,'#dropdown'))
# option = Select(dd_ele)
# option.select_by_value('OptionTWo')
# time.sleep(2)
# option.select_by_index(4)
# time.sleep(3)
driver.get('http://dummypoint.com/DragAndDrop.html')
# time.sleep(3)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)

drag = wait.until(ec.presence_of_element_located((By.ID,'drag')))
drop = wait.until(ec.presence_of_element_located((By.ID,'drop')))

# drag = driver.find_element(By.ID,'drag')
# drop = driver.find_element(By.ID,'drop')

action = ActionChains(driver)
action.click_and_hold(drag).perform()
action.release(drop)
time.sleep(2)


driver.quit()




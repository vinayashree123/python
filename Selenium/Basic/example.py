import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')


# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
# c_ele = driver.find_elements(By.NAME,'checkbox')
#
# for checkbox in c_ele:
#     checkbox_button = checkbox.get_attribute('value')
#     if checkbox_button == 'c2':
#         checkbox.click()
#         print('checkbox selected',checkbox.is_selected())
#         driver.implicitly_wait(10)
#         time.sleep(2)
#
# r_ele = driver.find_elements(By.NAME,'radio')
# for radio in r_ele:
#     r_button = radio.get_attribute('value')
#     if r_button == 'Button3':
#         radio.click()
#         time.sleep(4)

#scroll guesture
# ele = driver.find_element(By.ID,'submitbutton')
# action = ActionChains(driver)
# action.move_to_element(ele).perform()
# time.sleep(2)
#
# #dropdown
# ele = driver.find_element(By.ID,'dropdown')
# dd_options = Select(ele)
# dd_options.select_by_index(2)
# time.sleep(2)

#dragdrop
# driver.get('http://dummypoint.com/DragAndDrop.html')
# ele1 = driver.find_element(By.ID,'drag')
# ele2 = driver.find_element(By.ID,'drop')
#
#
# actions = ActionChains(driver)
# actions.click_and_hold(ele1).perform()
# actions.release(ele2)
# time.sleep(3)

#iframe
driver.get('http://dummypoint.com/Frame.html')

# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

ele = driver.find_elements(By.TAG_NAME,'iframe')

driver.switch_to.frame(3)
time.sleep(3)

# switch to iframe by name
# time.sleep(2)
# driver.switch_to.frame('farme2')





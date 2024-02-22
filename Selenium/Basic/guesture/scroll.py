import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Edge()

driver.get("http://www.dummypoint.com/Form.html")


wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])

# wait.until(ec.presence_of_element_located((By.LINK_TEXT,'Form'))).click()
# wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/nav/form/div/input'))).click()

wait.until(ec.presence_of_element_located((By.ID,'name'))).send_keys('vinaya')
wait.until(ec.presence_of_element_located((By.ID,'email'))).send_keys('vinaya@gmail.com')
wait.until(ec.presence_of_element_located((By.ID,'tech'))).send_keys('python')

post_button = wait.until(ec.presence_of_element_located((By.ID,'btnContactUs')))

action = ActionChains(driver)

wait.until(ec.presence_of_element_located((By.XPATH,'//*[@id="g"]'))).click()
wait.until(ec.presence_of_element_located((By.ID,'message'))).send_keys('hi')
captch = wait.until(ec.presence_of_element_located((By.ID,'captcha_image')))
wait.until(ec.presence_of_element_located((By.ID,'captcha'))).send_keys(captch.text)

action.move_to_element(post_button).perform()
post_button.click()
time.sleep(5)
driver.quit()

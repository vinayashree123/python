import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')


#by using id(for that add # before value of id)
# driver.find_element(By.CSS_SELECTOR,'#user_input').send_keys('vinaya')

#by using class_name(before that give .)
# driver.find_element(By.CSS_SELECTOR,'.entertext').send_keys('class2')

#using "tag_name[name=value]' with css attribute
# driver.find_element(By.CSS_SELECTOR,'input[name=textbox]').send_keys('css with tag_name')

#by_tag_name with class name "tag_name.class[name=value]"
# driver.find_element(By.CSS_SELECTOR,'input.entertext[name=textbox]').send_keys('by_tag & class with css')

#starting letter using ^
# driver.find_element(By.CSS_SELECTOR,"input[class^='en']").send_keys('codetolead_SLWC')

#ending letter using ^ find e;lement
# driver.find_element(By.CSS_SELECTOR,"input[name$='ox']").send_keys('codetolead_ELWN')

#find elemnt using contains substring - *
driver.find_element(By.CSS_SELECTOR,"input[class*='er']").send_keys('codetolead_for_substring')
time.sleep(3)
driver.quit()

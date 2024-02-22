import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('http://dummypoint.com/seleniumtemplate.html')

ele = driver.find_elements(By.ID,'menu')
for menu in ele:
    print(menu.text)


time.sleep(3)
driver.quit()

from selenium import webdriver

driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
driver.get("https://www.google.com")
driver.quit()

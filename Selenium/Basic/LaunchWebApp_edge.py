import time
from selenium import webdriver

# Create a Microsoft Edge driver
driver = webdriver.Edge()

# Load the Google website
driver.get("https://www.google.com")


time.sleep(5)

# Close the browser
driver.quit()

import os
import platform
import subprocess
import time
import logging
import requests
from appium.webdriver.appium_service import AppiumService
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from colorama import init, Fore, Style

# Initialize colorama for colored console output
init(autoreset=True)


def start_appium_server():
    appium_log_file = "appium_server_log.log"

    # Redirect stdout and stderr to the log file
    with open(appium_log_file, "w") as log_file:
        appium_service = AppiumService()
        appium_service.start(args=["-p", "4724", "--base-path", "/wd/hub"], stdout=log_file, stderr=log_file)

    print(f"{Fore.GREEN}Appium server started.")
    print(f"{Fore.YELLOW}Appium server logs:")
    print(f"{Fore.YELLOW}------------------")
    # Add a delay to allow the server to start
    time.sleep(10)


def stop_appium_server():
    if platform.system() == "Windows":
        subprocess.Popen("taskkill /F /IM node.exe", shell=True)
    else:
        os.system("killall -9 node")


def create_driver_session():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Pixel 3a",
        "platformVersion": "10",
        "appPackage": "com.android.settings",
        "appActivity": "com.android.settings.Settings",
        "automationName": "UiAutomator2",
    }

    print(f"{Fore.CYAN}Initializing driver session...")
    try:
        appium_url = "http://localhost:4724/wd/hub"
        print(f"{Fore.CYAN}Connecting to Appium server at:", appium_url)

        response = requests.post(f"{appium_url}/session", json={"desiredCapabilities": desired_caps})
        print(f"{Fore.CYAN}Appium server response:", response.text)

        driver = webdriver.Remote(appium_url, desired_caps)
        print(f"{Fore.GREEN}Driver session initialized successfully.")
        return driver
    except Exception as e:
        print(f"{Fore.RED}Error occurred while initializing driver session:", str(e))
        raise


def take_screenshot(driver, filename):
    driver.save_screenshot(filename)


def main():
    # Set up logging
    log_filename = "appium_log.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")
    logging.info("Appium Server started.")
    start_appium_server()
    print(f"{Fore.CYAN}Initializing driver session...")  # Add this line for debugging
    driver = create_driver_session()
    time.sleep(5)  # Add a delay to ensure the app is fully loaded
    # Example: Tap on "Connections"
    connection_element = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Connected devices"]')
    connection_element.click()
    time.sleep(2)  # Add a delay after tapping
    # Take a screenshots
    screenshot_filename = "settings_screenshot.png"
    take_screenshot(driver, screenshot_filename)
    logging.info("Screenshot saved: %s", screenshot_filename)
    # Close the driver session and stop the Appium server
    if 'driver' in locals():
        driver.quit()
    stop_appium_server()
    logging.info("Appium Server stopped.")


if __name__ == "__main__":
    main()

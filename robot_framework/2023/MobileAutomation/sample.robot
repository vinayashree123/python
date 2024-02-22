*** Settings ***
Library  AppiumLibrary

*** Test Cases ***
Launch the browser
    open application  http://127.0.0.1:4723/wd/hub   automationName=UiAutomator2  platformName=Android
    ---   platformVersion=13    browserName=edge
    go to url  http://google.com
    close application

*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
opening browser
    open browser  http://google.com     firefox
closeing browser
    close browser

*** Test Cases ***
Launch browser
    opening browser
    closeing browser



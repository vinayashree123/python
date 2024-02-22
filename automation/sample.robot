*** Settings ***
Library     Selenium2Library
Library     SeleniumLibrary
*** Variables ***

*** Test Cases ***
Sample Test Case
    [Documentation]    Google Test
    [Tags]    regression
    Open Browser    http://www.google.com    chrome
    Close Browser

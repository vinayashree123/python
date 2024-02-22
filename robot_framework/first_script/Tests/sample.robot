*** Settings ***
Library     Selenium2Library
Library  selenium2library
Library  Selenium2Library
*** Variables ***

*** Test Cases ***
Sample Test Case
    [Documentation]    Google Test
    [Tags]    regression
    Open Browser    http://www.google.com    edge
    Close Browser

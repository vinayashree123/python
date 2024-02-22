*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Access Website Without Login
    Open Browser    https://1-thing.in/#/timesheet    edge
    Set Selenium Implicit Wait    10s

    # You can add further interactions with the website here

    # If you want to close the browser at the end of the test, you can add:
    # Close Browser

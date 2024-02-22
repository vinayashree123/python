*** Settings ***
Library     Selenium2Library
*** Test Cases ***
this is first test case
    [Documentation]  this is first test case
    [Tags]  1006 smoke contact
    log  start case
    #initialize selelenium
    set selenium speed  .2s
    set selenium timeout  5s
    open browser    https://www.google.com    edge
    sleep   3s

    #resize browser window
    set window position     x=341   y=169
    set window size     width=1935     height=1090
    close browser

*** Keywords ***

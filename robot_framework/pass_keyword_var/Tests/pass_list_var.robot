*** Settings ***
Library  Selenium2Library
*** Variables ***
*** Test Cases ***
this is first test
    @{url & browser} =  set variable    http://www.google.com  chrome
    begin to test   @{url & browser}
*** Keywords ***
begin to test
    [Arguments]  @{url & browser}
    open browser    @{url & browser} [0]    @{url & browser} [1]
    close browser


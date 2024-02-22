*** Settings ***
Library  Selenium2Library
*** Variables ***
*** Test Cases ***
this is first test
    begin to test   http://www.google.com   chrome
*** Keywords ***
begin to testz
    [Arguments]  ${url}  ${browser}
    open browser    ${url}  ${browser}
    close browser


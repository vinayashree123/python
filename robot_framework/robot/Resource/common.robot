*** Settings ***
Library  Selenium2Library
*** Variables ***
${BROWSER} =    chrome
${URL} =    https://automationplayground.com/front-office/

*** Keywords ***
Begin web test
    open browser  about:blank   ${BROWSER}

End web test
    close all browsers



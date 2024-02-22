*** Settings ***
Library  Selenium2Library
*** Variables ***
${BROWSER} =    chrome
${URL} =    https://outlook.live.com
${SIGNIN_ELEMENT}   =   css=body > header > div > aside > div > nav > ul > li:nth-child(2) > a

*** Test Cases ***
opening the browser
    open browser    ${URL}  ${BROWSER}
    wait until page contains element    xpath=/html/body/header/div/aside/div/nav/ul/li[2]/a
signin
    click link  xpath=/html/body/header/div/aside/div/nav/ul/li[2]/a
    sleep   5s
valid credentials
    input text  css=#i0116    vinayashree.naganuri@capgemini.com
    click element  xpath=//*[@id="idSIButton9"]
    sleep  15s
#    wait until page contains element  xpath=//*[@id="id__10"]
    wait until page contains element    xpath=//*[@id="id__173"]


*** Settings ***
Library     Selenium2Library

*** Variables ***
${BROWSER} =    edge
${URL} =    cd
${VALID_USER_EMAIL} =   vinayashree@gmail.com
${VALID_USER_PASSWORD} =    1234
*** Test Cases ***
this is first test case
    [Documentation]  this is first test case
    [Tags]  1006 smoke contact
    log  start case
    #initialize selelenium
    #set selenium speed  .2s
    #set selenium timeout  5s
    #open browser    https://www.lambdatest.com/blog/robot-framework-tutorial/  chrome
    #sleep   3s
    open browser    ${URL}  ${BROWSER}

    #resize browser window
    set window position     x=3   y=16
    set window size     width=1935     height=1090

    #click link      xpath=//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a

    #click element  link=Sign Up

    click element  link=Login

    input text  id=user_email   ${VALID_USER_EMAIL}
    input text  id=user_password    ${VALID_USER_PASSWORD}

    click button  id=user_login

    close browser


*** Keywords ***

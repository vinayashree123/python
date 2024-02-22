*** Settings ***
Library  Selenium2Library
*** Keywords ***
*** Variables ***
${url}  =   https://rahulshettyacademy.com/AutomationPractice/
${browser}  Chrome

*** Test Cases ***
first test case
    open browser    ${url}  ${browser}}
    select radio button  radioButton  radio2
    sleep  2s
#    select checkbox  id/class/name
    select checkbox     checkBoxOption1
    sleep  2s
    select checkbox     checkBoxOption2
    sleep  2s
    unselect checkbox   checkBoxOption1
    sleep  2s
    select from list by label  dropdown-class-example   Option1
    sleep  2s
    select from list by index  dropdown-class-example   2

    element should be visible  xpath=//*[@id="name"]
    sleep  2s
    element should be enabled  xpath=//*[@id="name"]
    sleep  2s
    input text  xpath=//*[@id="name"]   vinaya
    sleep  2s
    clear element text  xpath=//*[@id="name"]
    sleep  2s

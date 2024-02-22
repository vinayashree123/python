*** Settings ***
Library           SeleniumLibrary
Resource          C:/Users/vnaganur/PycharmProjects/robot_framework/2023/webAutomation/Resources/common.robot

*** Variables ***
${reg_url}        https://www.way2automation.com/way2auto_jquery/index.php
${username}       rahularora1423
${password}       askjdbfskjdfs

*** Test Cases ***
Launch Browser
    Open Browser   ${reg_url}   firefox

Fill Registration Form
    Input Text     name                  vina
    Input Text     phone                 8494889325
    Input Text     email                 vinayashreenaganuri5@gmail.com
    Input Text     city                  belagaum
    Select From List By Label    country   Guam
    Input Text     //*[@id="load_form"]/fieldset[6]/input             ${username}
    Input Text     //*[@id="load_form"]/fieldset[7]/input              ${password}
#    Wait Until Element Is Visible  //input[@class='button' and @type='submit']  10s
#    Click Element  //input[@class='button' and @type='submit']



close browser after fill form
    closeing browser

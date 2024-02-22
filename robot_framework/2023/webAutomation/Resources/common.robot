*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${reg_url}        https://www.way2automation.com/way2auto_jquery/index.php
${username}       rahularora1423
${password}       askjdbfskjdfs

*** Keywords ***
opening browser
    open browser  http://google.com     firefox
closeing browser
    close browser

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


*** Settings ***
Library  Selenium2Library

*** Variables ***

*** Test Cases ***
#filling the website
#    open browser  https://rahulshettyacademy.com/loginpagePractise/#    chrome
#    sleep   3s
#    input text  id=username     rahulshettyacademy
#    input text  id=password     learning
#    select radio button     radio     admin
##    handle alert  10 seconds    accept
##    select radio button
##    click button  id=okayBtn
##    wait until page contains  id=cancelBtn    timeout=20s
##    wait until keyword succeeds     4s
##    handle alert  accept
##    select from list by label  class_name label_name
#     Select From List By Label    class=form-control    Student
#    select checkbox  terms
#    sleep  4
#    click button  id=signInBtn
#    sleep  5
#    click button  xpath=/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[1]/div/div[2]/button
##    click element  class=btn btn-info
#    click button  xpath=/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[4]/div/div[2]/button
#    select card  css=body > app-root > app-shop > div > div > div.col-lg-9 > app-card-list > app-card:nth-child(1) > div > div.card-footer > button()
#    click link  css=#navbarResponsive > ul > li > a
#    sleep   20s
#
#    close browser
nav from one link to another
    open browser  https://rahulshettyacademy.com/loginpagePractise/#    chrome
    go to  https://rahulshettyacademy.com/documents-request
    ${email}    get text   xpath=//*[@id="interview-material-container"]/div/div[2]/p[2]/strong/a
    go back
    input text  id=username     ${email}
    input password  id=password     learning
    sleep  10s
#    select radio button     radio     admin
#    Select From List By Label    class=form-control    Student
#    select checkbox  terms
#    sleep  4
#    click button  id=signInBtn

create list and display element
    @{expectedlist} =   create list  iphone X   Samsung Note 8   Nokia Edge     Blackberry
    ${element}


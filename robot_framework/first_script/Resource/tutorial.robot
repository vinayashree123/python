*** Settings ***
Library     Selenium2Library

*** Keywords ***
check page contain login button
    #page should contain  Category
    page should contain element  xpath=//*[@id="navbarCollapse"]/div[2]/div/a

click on login
    click element  link=Login

enter email and password
    input text  id=user_email  vinayashreenaganuri1868@gmail.com
    input text  id=user_password  Vina@1234

click user login
    click button  id=user_login



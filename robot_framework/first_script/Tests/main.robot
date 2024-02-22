*** Settings ***
Documentation  this one has basic test suite
Resource  C:/Users/vnaganur/PycharmProjects/robot_framework/first_script/Resource/tutorial.robot

Resource  C:/Users/vnaganur/PycharmProjects/robot_framework/first_script/Resource/common.robot

*** Test Cases ***
this is contain all test suite
    common.opening browser

    tutorial.click on login
    tutorial.enter email and password
    tutorial.click user login
    common.closeing browser



*** Settings ***
Documentation  This test suite contain the robotframework testcase
Library  Selenium2Library
Resource  C:/Users/vnaganur/PycharmProjects/robot_framework/robot/Resource/robotApp.robot
Resource  C:/Users/vnaganur/PycharmProjects/robot_framework/robot/Resource/common.robot
Test Setup  Begin web test
Test Teardown  End web test

#robot -d Results Tests/robotscript.robot
*** Variables ***


*** Keywords ***
*** Test Cases ***
should be able to access "Team" page
    [Documentation]  this is test 1
    [Tags]  test1
    log  testcase 1
    robotApp.Go to landing page
    robotApp.Go to "Team" page


"Team" should meet the requirements
    [Documentation]  this is test 2
    [Tags]  test2
    log  testcase 2
    robotApp.Go to landing page
    robotApp.Go to "Team" page
    robotApp.validate "Team" page




#check page contain
#    page should contain element  ${TEAM_BUTTON}
#    #page should contain button  ${TEAM_BUTTON}
#submit form
#    click link  ${TEAM_BUTTON}
#    wait until page contains    ${HOME_PAGE_CONTAIN}
#    close browser

*** Settings ***
Library  Selenium2Library
*** Variables ***
${TOP_NOV_LINK} =  css=#bs-example-navbar-collapse-1 > ul > li:nth-child(5) > a
*** Keywords ***
select "Team" page
#    click link  Team
    click element   ${TOP_NOV_LINK}
    sleep  3s

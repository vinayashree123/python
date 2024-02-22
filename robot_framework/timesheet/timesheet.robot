*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
Filling Time Sheet
    Set Selenium Implicit Wait    10s


    #click to change default
    click element  //*[@id="app"]/div/header/div/div[2]/div[1]/div/span
    click element  //*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div
    click element  //*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span/i

    #close setting
    click element  css=#app > div > div:nth-child(2) > div.vodal-dialog > span

    click link  css:#app > div > div.layout-w.sidebar > div.sidebar-nav-wrap > nav > ul > li.nav-item.active > a

*** Test Cases ***
Basic Test Case
    Open Browser    https://1-thing.in/#/timesheet    edge
    Set Selenium Implicit Wait    10s
    Input Text    email    vidyashri.naganuri   #379680

    # The correct usage of select from list by label
    Select From List By Label    //*[@id="app"]/div/div[2]/div/div/div/div/form/div[1]/div/select    @neosoftmail.com

    # Enter MPIN
    ${mpin} =    Evaluate    "239868"
    Input Text    xpath=//*[@id="app"]/div/div[2]/div/div/div/div/form/div[2]/div/div[1]/input    ${mpin}

    # Click the submit button
    Click Button    //*[@id="btn_do_login"]

    FOR    ${i}    IN RANGE    1    # 24 hours in a day
        # Execute the "Filling Time Sheet" part
        Filling Time Sheet
        # Sleep for one hour (3600 seconds)
        Sleep    30
    END


#no logout
#     FOR    ${i}    IN RANGE    86400   # 86400 seconds in a day
#        # Add tasks to be repeated here
#        Click Element    //*[@id="some-element"]   # Example task
#
#        #click to change default
#        click element  //*[@id="app"]/div/header/div/div[2]/div[1]/div/span
#        click element  //*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div
#        click element  //*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span/i
#
#    #close setting
#        click element  css=#app > div > div:nth-child(2) > div.vodal-dialog > span
#        Set Selenium Implicit Wait    10s
#
#        click link  css:#app > div > div.layout-w.sidebar > div.sidebar-nav-wrap > nav > ul > li.nav-item.active > a
#        Sleep    1   # Sleep for 1 second in each iteration
#    END





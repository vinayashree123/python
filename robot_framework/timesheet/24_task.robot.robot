*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
Basic Test Case
    Open Browser    https://1-thing.in/#/login    edge
    Set Selenium Implicit Wait    10s
    Input Text    email    vidyashri.naganuri   #379680

    # The correct usage of select from list by label
    Select From List By Label    //*[@id="app"]/div/div[2]/div/div/div/div/form/div[1]/div/select    @neosoftmail.com

    # Enter MPIN
    ${mpin} =    Evaluate    "123090"
    Input Text    xpath=//*[@id="app"]/div/div[2]/div/div/div/div/form/div[2]/div/div[1]/input    ${mpin}

    # Click the submit button
    Click Button    //*[@id="btn_do_login"]

no logout
    click element  //*[@id="app"]/div/header/div/div[2]/div[1]/div/span
    click element  //*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div
    click element  //*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span/i

    #close setting
    click element  css=#app > div > div:nth-child(2) > div.vodal-dialog > span

    sleep   100

#    click on add task


#    click link  css:#app > div > div.layout-w.sidebar > div.side

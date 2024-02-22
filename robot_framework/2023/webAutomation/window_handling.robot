*** Settings ***
Library           SeleniumLibrary
Resource          C:/Users/vnaganur/PycharmProjects/robot_framework/2023/webAutomation/Resources/common.robot


*** Test Cases ***
handling window
    Launch Browser
    Fill Registration Form
    click link  link:ENTER TO THE TESTING WEBSITE
    sleep   5s
#    scroll element into view  xpath://*[@id="wrapper"]/div/div/div[5]/ul/li/a/figure
    click element  xpath://*[@id="wrapper"]/div/div/div[5]/ul/li/a/figure
    sleep   5s
    @{window_handle}=   get window handles
    log to console  ${window_handle}
    sleep   5s
    switch window   ${window_handle}[1]
    input text  name    vina
    choose file     xpath://html/body/section/div[1]/div/div/form/fieldset[9]/input  C:\\Users\\vnaganur\\OneDrive - Capgemini\\Pictures\\imagecomparasion.png
    close window
    switch window   ${window_handle}[0]
    close window
    closeing browser


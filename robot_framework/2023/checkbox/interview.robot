*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
opening the browser
    open browser  https://practice.expandtesting.com/checkboxes     edge
    checkbox demo


*** Keywords ***
checkbox demo
    @{checkbox}=    get webelements  xpath://*[@id="checkboxes"]
#    log to console  @{checkbox[0]}
    select checkbox    xpath://*[@id="checkbox1"]
    FOR     ${i}   IN  @{checkbox}
        select checkbox  ${i}
        checkbox should be selected     xpath://*[@id="checkbox1"]
        sleep  2
    END


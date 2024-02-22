*** Settings ***
Library     SeleniumLibrary
*** Variables ***
*** Test Cases ***
example 1
    open browser  https://www.wikipedia.org/    edge
    wait until element is visible   //*[@id="searchInput"]
#    select from list by label   name:language    हिन्दी
    select from list by index  name:language    2
#     select from list by value  name:language    ast
#    @{element}=     get webelements  xpath://select[@id='searchLanguage']//option
#    ${count}=   get length  ${element}
#    log to console  the value are ${count}
#    FOR   ${ele}  IN  ${element}
##        ${text}=    get text    ${ele}
#         ${text}=   get element attribute  ${ele}   lang
#        log to console  the elements in options are ${text}
#    END
#    sleep  5
    close browser


#demo 2
#    open browser  https://www.wikipedia.org/    edge
#    wait until element is visible   //*[@id="searchInput"]
#    select from list by value       name="language"     af

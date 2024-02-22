*** Settings ***
Library     SeleniumLibrary
*** Variables ***
*** Test Cases ***
example 1
    open browser  https://www.wikipedia.org/    edge
    wait until element is visible   //*[@id="searchInput"]
total link
    @{link}=    get webelements  //a
    ${link_count}=  get length  ${link}
    log to console  total links are ${link}
handle multi link
    @{child_ele}=   get webelements     xpath://*[@id="www-wikipedia-org"]/div[8]/div[3]//a
    ${count_child_ele}=     get length  ${child_ele}
    log to console  the total child link are ${count_child_ele}
    FOR     ${i}    IN  ${child_ele}
        ${text}=    get text    ${i}
        log to console  ${text}
    END

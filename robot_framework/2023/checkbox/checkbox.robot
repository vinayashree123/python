*** Settings ***
Library     SeleniumLibrary
*** Variables ***
*** Test Cases ***
example 1
    open browser  http://www.tizag.com/htmlT/htmlcheckboxes.php      edge
    page should contain checkbox  xpath:/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]/input[1]
#    select checkbox  xpath://div[4]/input[1]
#    unselect checkbox  xpath://div[4]/input[2]
#    select checkbox  xpath://div[4]/input[3]
#    select checkbox  xpath://div[4]/input[4]
    sleep  4
testcase 2
    @{checkbox}=    get webelements  xpath://div[4]/input
    log   ${checkbox[0]}
    ${count}=   get length  ${checkbox}
    log to console  ${count}

#    to get text of web element
    FOR  ${i}    IN     @{checkbox}
        select checkbox    ${i}
        sleep  4
    END


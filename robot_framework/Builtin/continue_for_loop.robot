*** Settings ***
Library  SeleniumLibrary
*** Variables ***
@{list}     item1   item2   item3   item4
*** Test Cases ***
skiping the execution of for loop using continue
    FOR  ${var}  IN  @{list}
        Run Keyword If  '${var}' == 'item3'     continue for loop
        log to console  ${var}
    END
breaking the execution of for loop using break
    FOR  ${var}  IN  @{list}
        Run Keyword If  '${var}' == 'item3'     exit for loop if    True
        log   ${var}
    END

skiping the execution of for loop using continue for loop
    FOR  ${var}  IN  @{list}
        continue for loop if    '${var}' == 'item3'
        log to console  ${var}
    END
convert to binary and
    ${result} =     convert to binary  10
    log to console  ${result}
    ${result1} =     convert to binary  F  base=16	 prefix=0b
    log to console  ${result1}

create dictionary 1
    ${dict} =   create dictionary  vina=23  pratushya=22    varsh=21


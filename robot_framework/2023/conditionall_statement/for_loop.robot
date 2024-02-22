*** Variables ***
@{list}=    item1   item2   item3

*** Test Cases ***
for loop
    FOR     ${i}    IN RANGE    5
        log to console  ${i+1}
    END

for loop in range
    FOR     ${i}    IN RANGE    1   10  2
        log to console  ${i}
    END

for loop in range and exit for loop
    FOR     ${i}    IN RANGE    1   10
        log to console  ${i}
        exit for loop if  ${i}==5
    END
for loop with list item
    FOR    ${i}    IN   @{list}
        log to console  ${i}
        exit for loop if    '${i}' == 'item2'
    END

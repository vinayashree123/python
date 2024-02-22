*** Settings ***

*** Variables ***
${name} =   'Vinaya'
${num1}=    10
${num2}=    18

*** Test Cases ***
IF else Block
    IF    ${num1} == ${num2}
        log to console    both are equal
    ELSE
         log to console    both are NOT equal
    END

if
    IF    1 == 1
        log to console    This line IS executed.
    END

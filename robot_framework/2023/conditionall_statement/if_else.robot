*** Settings ***
*** Variables ***
${name}=     vinayaa
${num1}=    1
${num2}=    10
*** Test Cases ***
if test cases
    IF  "${name}" == "vinaya"
        log   my name is vinaya
    END
if else test cases
    IF  "${name}" == "vinaya"
        log   my name is vinaya
    ELSE
        log to console  my name is not vinaya
    END
number comparision
    IF  ${num1} == ${num2}
        log to console  both equal
    ELSE IF ${num1} > ${num2}
        log to console  ${num1} is greater than ${num2}
    ELSE
        log to console  ${num2} is greater than ${num1}
    END
And or operation
    IF  ${num1} < ${num2} and ${num2} < 9
        log to console  ${num2} is between 0 and 9
    ELSE
        log to console  ${num2} is not between 0 and 9
    END

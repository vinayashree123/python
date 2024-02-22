*** Settings ***
Library  selenium2library
*** Test Cases ***
test case 1
    Do something
    Do another thing
test case 2
    do another thing
    do something else

*** Keywords ***
Do something
    log  iam doing somthing...
Do another thing
    log  iam doing another thing
do something else
    log  iam doing something else



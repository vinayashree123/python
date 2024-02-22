*** Settings ***
*** Variables ***
${var}  =   hello how

*** Test Cases ***
set the variable
    ${name} =   set variable    vinaya ramu
    log     ${name}

var demonstation
    log     ${var}

var demonstation1
    log     ${var}




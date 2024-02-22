*** Settings ***

*** Variables ***
${var}  = 1
@{list}  =   1   2   3   4
&{dict_var}  =   name=vina   age=23

*** Test Cases ***
set variable
    ${name} =   set variable  vina
    log to console  ${name}

scalar var demo
    log to console  ${var}

List var demo
    FOR  ${i}  IN  @{list}
        log to console  ${i}
    END

accesing the list var
    log to console  ${list[0]}

dictionary demo
    log     ${dict_var.name}

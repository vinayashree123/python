*** Settings ***
*** Variables ***
#scalar var
${name}=    vina    ramu
#list var
@{fruits}=  banana  apple   sapota
@{city}=    Delhi    Mumbai    Goa
#dict var
&{dict_var}=    name=vina   id=m109
*** Test Cases ***
list variable demo
    log     ${name}
    log     ${fruits}[0]
    log     ${fruits}[1]
    log     ${city}[0]
    log     ${dict_var.name}


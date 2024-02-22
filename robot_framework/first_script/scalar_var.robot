*** Settings ***
Library  Selenium2Library
*** Variables ***
${my_variable} =    hello there
*** Test Cases ***
set var in test case
    ${my_new_variable} =  set variable  iam vina
    log  ${my_new_variable}
variable demonstration
    log  ${my_variable}
variable demonstration 2
    log  ${my_variable}


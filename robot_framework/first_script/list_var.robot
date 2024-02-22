*** Settings ***
Library  Selenium2Library
*** Variables ***
${my_variable} =    hello there     hi      vinayashree
*** Test Cases ***
set var in test case
    ${my_new_variable} =  set variable  item1   item2   item3
    log  ${my_new_variable} [0]
    log  ${my_new_variable} [1]
    log  ${my_new_variable} [2]
variable demonstration
    log  ${my_variable} [0]
    log  ${my_variable} [1]
    log  ${my_variable} [2]

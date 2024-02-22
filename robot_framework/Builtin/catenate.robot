*** Settings ***
Library  Selenium2Library
*** Variables ***
${first_name} =     vina
${second_name} =     naganuri
*** Test Cases ***
example test case
    ${result} =  catenate   ${first_name}   ${second_name}
    log  ${result}
    #guiuy
    comment  ${result}
testcase 2
    ${result1} =     Catenate    Hello    |    world    |    !
    log  ${result1}
    comment     nothing to do


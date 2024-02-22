*** Settings ***
*** Variables ***
#global varible can be accessibe in the testcase
${MY_VAR} =  HELLO  HOE
*** Test Cases ***
set var in test case
    #testcase/keyword variable are not accesible inside different testcase
#    ${my_new_variable} =  set variable  iam vina
#    log  ${my_new_variable}
    log  ${MY_VAR} [0]
different testcase
    #log  ${my_new_variable}
    log  ${MY_VAR} [1]

*** Settings ***
Documentation  this contain built in test
Library  Selenium2Library
Library  Dialogs

*** Variables ***
${GLOBAL} =     VINAYA
${URL}  =   https://www.youtube.com/watch?v=Gf-3arXnkRY
${BROWSER}  = chrome
*** Test Cases ***
Declare and set variable
    ${set_variable} =   set variable  hello world
    set test variable   ${some_test-data}   test_data
    set suite variable  ${some_suite_data}  suitee
    set global variable     ${some_global_data}  global
    pause execution
    log  ${some_suite_data}
    log to console  ${some_test-data}

Logging stuff
    [Tags]  Builtin
    comment     ${unset_data}
    comment     ${set_variable}
    log     i have to do
    log many  iam doing     i will do   i can do
    log  ${GLOBAL}
    log to console  some_test-data
#    repeat keyword  3 Times     hi hello fill

Ignore failure in the test
    open browser    http:www.google.com     chrome
    run keyword and continue on failure  wait until page contains  the text not exit
    close browser

repeat keyword
    #repeat keyword  times_to_repeat    keyword_name
    repeat keyword  3 Times  say something funny

Dialog library
    ${browser} =   get selection from user  Which browser  chrome  ie  firefox
    #set global variable  ${BROWSER}     ${browser}

    open browser    ${URL}    ${browser}
    close browser
    execute manual step  do something
#Dialog2
#    ${value1}   get value by user   1   2   3
#    ${value2}   get value by user   12   22   23
#    ${result}   catenate    ${value1}       ${value2}
#    log ${result}

*** Keywords ***
say something funny
    log  How are you



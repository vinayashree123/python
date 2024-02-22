*** Settings ***
Documentation
Library  OperatingSystem
*** Keywords ***
enter usename
    log     ${My_Dict}[name]
*** Variables ***
@{list}   item1  item2  item3
&{My_Dict}      name=veena      password=veena@123

*** Test Cases ***
Test1
    [Tags]  demo    demo1
    log     ${list}[0]
    log     ${My_Dict}[name]

Test2
    enter usename


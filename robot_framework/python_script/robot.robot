*** Settings ***
Library  pythonfile.py

*** Test Cases ***
#Testcase 1
#    ${out} =    pythonfile.add  ${10}  ${30}
#    should be equal  ${out}     ${40}
#    log to console  ${out}
Testcase 2
    ${result} =     custom keyword  ${1}    ${2}
    should be equal  ${result}  ${3}
    log to console  ${result}

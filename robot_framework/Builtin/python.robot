*** Settings ***
Library     OperatingSystem
*** Test Cases ***
Run Python Script
    ${output}   Run Process     C:\Users\vnaganur\PycharmProjects\robot_framework\Builtin\python.py  arg1 arg2
    Log ${output.stdout}
    Log ${output.stderr}

*** Settings ***
Library     Selenium2Library

*** Variables ***
${url}           www.amazon.com
${browser}       Chrome
${search_term}   ferrari 458

*** Test Cases ***
User Can Search Product
    Open Browser    ${url}    ${browser}
    #Input Text      id=twotabsearchtextbox    ${search_term}

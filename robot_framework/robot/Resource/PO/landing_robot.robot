*** Settings ***
Library  Selenium2Library
*** Variables ***
${NAVIGATE_TO_LANDING_PAGE} =  css=#mainNav > div > div.navbar-header.page-scroll > a
*** Keywords ***
Navigate To
    go to   ${URL}
verify page loaded
    wait until page contains element    ${NAVIGATE_TO_LANDING_PAGE}



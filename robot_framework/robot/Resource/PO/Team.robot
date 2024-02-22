*** Settings ***
Library  Selenium2Library
*** Variables ***
${NAVIGATE_TO_TEAM_PAGE} =  css=#team > div > div:nth-child(1) > div > h2

*** Keywords ***
verify page loaded
    wait until page contains element    ${NAVIGATE_TO_TEAM_PAGE}
verify page contents
    ${ELEMENT_TEXT} =  get text  ${NAVIGATE_TO_TEAM_PAGE}
    should be equal as strings      ${ELEMENT_TEXT}     Our Amazing Team    ignore_case=true
    #element text should be  ${NAVIGATE_TO_TEAM_PAGE}    Our Amazing Team

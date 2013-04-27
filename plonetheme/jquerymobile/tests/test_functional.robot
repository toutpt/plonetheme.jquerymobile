*** Settings ***

Resource  plone/app/robotframework/selenium.robot

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Plone is installed
    Go to  ${PLONE_URL}
    Import library Dialogs
    Pause Execution
    Page should contain  Powered by Plone

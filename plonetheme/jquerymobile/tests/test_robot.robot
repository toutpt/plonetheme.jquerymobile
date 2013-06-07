*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Site Administrator can access control panel
    Given I'm logged in as site owner
     When I open the personal menu
     Then I see the Site Setup -link

*** Keywords ***

I'm logged in as test user
    Log in as test user
    Go to  ${PLONE_URL}

I'm logged in as site owner
    Log in as site owner
    Go to  ${PLONE_URL}

I open the personal menu
    Click link  css=#user-name

I see the Site Setup -link
    Element should be visible  css=#personaltools-plone_setup

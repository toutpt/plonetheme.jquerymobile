*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/saucelabs.robot
Resource  plonetheme/jquerymobile/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open SauceLabs test browser
Test Teardown  Run keywords  Report test status  Close all browsers

*** Test Cases ***

I can open the login form
    Given I'm on the home page
     When I click on the 'user' icon
     Then I see the login form

I can open the search form
    Given I'm on the home page
     When I click on the 'search' icon
     Then I see the search form

I can browse the global sections
    Given I'm logged in as site owner
     When I add a folder 'section 1'
      And I add a folder 'sub-section 2'
      And I click on the 'folder-open' icon
     Then I see the sections

Site Owner can access control panel
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

I'm on the home page
    Go to  ${PLONE_URL}

I click on the '${ICON}' icon
    JQMobile:Click '${ICON}' icon

I see the login form
    Element should be visible  css=#__ac_name
    Element should be visible  css=#__ac_password

I see the search form
    Element should be visible  css=input[name="SearchableText"][data-type="search"]

I add a folder '${title}'
    JQMobile:Add folder  ${title}

I see the sections
    Element should be visible  css=#popup-globalsection
    Element should be visible  css=#portaltab-index_html
    Element should be visible  css=#portaltab-section-1
    Element should not be visible  css=#portaltab-sub-section-2

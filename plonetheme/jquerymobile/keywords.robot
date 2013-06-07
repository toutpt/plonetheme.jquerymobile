*** Settings ***

Documentation  *WARNING* This resource is not stable yet and keywords may be
...            renamed, removed or relocated without notice.

Resource  plone/app/robotframework/selenium.robot


*** Keywords ***

JQMobile:Click '${ICON}' icon
    Click link  css=[data-icon="${ICON}"]

JQMobile:Open left panel
    JQMobile:Click 'bars' icon
    Wait Until Page Contains Element  css=#panel-left

JQMobile:Add folder
    [arguments]  ${title}

    JQMobile:Open left panel
    Click Link  css=#plone-contentmenu-factories a
    Wait Until Page Contains Element  css=a#folder
    Click Link  css=a#folder
    Wait Until Page Contains Element  css=#archetypes-fieldname-title input
    Input Text  title  ${title}
    Click Button  Save
    Page should contain  ${title}
    Element should contain  css=#parent-fieldname-title  ${title}

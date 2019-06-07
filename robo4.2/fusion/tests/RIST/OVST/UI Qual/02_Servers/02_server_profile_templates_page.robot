*** Settings ***
Documentation    Server Profile Template Page Test Suite
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  spt  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}

*** Test Cases ***
Dialog 'Create Server Profile Template' Elements Should Appear As Expected
    [Documentation]  Server Profile Template Page Dialog 'Create Server Profile Template' Should Diaplay Elements As Expected
    ...    \n Navigate to Server Profile Templates page
    ...    \n Click "Create server profile template"
    ...    \n Create Server Profile Template" dialog should be visible
    ...    \n "Create" button should be visible and should have "hp-primary" class
    ...    \n "Element Should Be Visible  css=#cic-profile-create.hp-button.hp-primary
    ...    \n "Create+" button should be visible
    ...    \n Iterate through items in panel selection menu
    ...    \n Click the items and verify they're scrolled into view
    ...        (note that this should be controlled by a generic function that you can use to select panels on any other page)
    ...    \n Click cancel button

    Open Sub Menu   Servers   Server Profile Templates
    Navigate to Page  Server Profile Templates
    Click Link        link=Create server profile template
    Dialog Should Be Visible  Create Server Profile Template
    ${panels}=  Create List From Action or Panel Drop Menu  cic-profile-add-panel-selector
    :FOR  ${panel}  in  @{panels}
    \    Select Item From Action or Panel Drop Menu  cic-profile-add-panel-selector  ${panel}
    \    Panel Should Be Visible  ${panel}
    Page Should Contain Button    css=#cic-profile-create.hp-primary
    Page Should Contain Button    id=cic-profile-createAgain
    Click Button  id=cic-profile-add-cancel
    Dialog Should Not Be Visible  Create Server Profile Template

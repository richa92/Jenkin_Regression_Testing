*** Settings ***
Documentation    Hardware Setup Page functionality
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  hardwaresetup  tbird
Test Timeout     ${TEST_TIMEOUT}


*** Test Cases ***
Page Elements Should Appear as Expected
    [Documentation]  Hardware Setup Page Elements Should Appear as Expected
    ...    \n Navigate to Hardware Setup page
    ...    \n Actions menu should be visible
    ...    \n Click Actions menu
    ...    \n Click "Add Remote Enclosures"
    ...    \n "Add Remote Enclosures"  Dialog should be visible
    ...    \n Ensure and verify text can be input into the "Remote Enc IPV6 address" field
    ...    \n "Add" button should be visible and as primary in Add Remote Enclosures Dialog box
    ...    \n "Add+" button should be visible in Add Remote Enclosures Dialog box
    ...    \n Click Cancel Button in Add Remote Enclosures Dialog box
    ...    \n "Add Remote Enclosures" Dialog box should not be visible

    Open Sub Menu   Appliance   Hardware Setup
    Navigate to Page                  Hardware Setup
    Select Item From Action or Panel Drop Menu  cic-hwsetup-actions  Add remote enclosures
    Dialog Should Be Visible          Add Remote Enclosures
    Dialog Element Should Be Visible  css=#cic-hwsetup-add-button.hp-primary
    Dialog Element Should Be Visible  id=cic-hwsetup-addagain-button
    Dialog Element Should Be Visible  id=cic-hwsetup-add-cancel
    Click Button                      id=cic-hwsetup-add-cancel
    Dialog Should Not Be Visible      Add Remote Enclosures

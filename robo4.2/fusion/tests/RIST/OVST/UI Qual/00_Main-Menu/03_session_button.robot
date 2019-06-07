*** Settings ***
Documentation    Session Button functionality
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  mainmenu  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}

*** Test Cases ***
Edit Dialog Elements Should Appear As Expected
    [Documentation]    Click session control button
    ...    \n Flyout should be visible
    ...    \n Edit link should be visible
    ...    \n Logout link should be visible
    ...    \n Click edit link
    ...    \n Edit Administrator dialog should be visible
    ...    \n OK button should be visible/primary
    ...    \n Click cancel button
    ...    \n Edit Administrator dialog should not be visible

    Click Element  css=div.hp-icon.hp-session
    Element Should Be Visible  css=#hp-session-flyout.hp-active
    Element Should Be Visible  id=hp-session-user-edit
    Click Element  id=hp-session-user-edit
    Dialog Should Be Visible  Edit Administrator
    Element Should Be Visible  css=#fs-usersettings-edit.hp-primary
    Click Button  id=fs-usersettings-edit-cancel
    Dialog Should Not Be Visible    Edit Administrator

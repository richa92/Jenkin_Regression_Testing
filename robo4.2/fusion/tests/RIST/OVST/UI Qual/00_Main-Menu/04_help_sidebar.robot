*** Settings ***
Documentation    Help Sidebar Functionality
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout and Close Browser
Force Tags       smoke  mainmenu  tbird  c7000
Test Timeout     ${TEST_TIMEOUT}

*** Test Cases ***
Pressing the Help Button Should Toggle Display of the Help Sidebar
    [Documentation]  Pressing the Help Button Should Toggle Display of the Help Sidebar
    ...    \n Click Help Icon
    ...    \n Help sidebar should be visible
    ...    \n Label should be "Help"
    ...    \n Click Help Icon
    ...    \n Help sidebar should not be visible

    Click Element  css=div.hp-icon.hp-help
    Element Should Be Visible  id=hp-help-flyout
    Element Should be Visible  xpath=//div[@id='hp-help-flyout']//h1[text()='Help']
    Click Element  css=div.hp-icon.hp-help
    Element Should Not be Visible  xpath=//div[@id='hp-help-flyout']//h1[text()='Help']
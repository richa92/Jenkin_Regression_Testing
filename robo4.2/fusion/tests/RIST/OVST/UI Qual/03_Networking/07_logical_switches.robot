*** Settings ***
Documentation      Logical Switches Page test suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout And Close Browser
Force Tags         smoke  logicalswitches  c7000
Test Timeout     ${TEST_TIMEOUT}


*** Test Cases ***
'Create logical switch' Dialog Elements Should Appear As Expected
    [Documentation]  Logical Switches Page dialog 'Create logical switch' Elements Should Appear As Expected
    ...    \n Navigate to LS page
    ...    \n Click "Create Logical Switch"
    ...    \n "Create Logical Switch" Dialog box Should be visible
    ...    \n "Close" button should be visible
    ...    \n Click "Close" button in "Create Logical Switch" Dialog box
    ...    \n "Create Logical Switch" Dialog box Should not be visible

    Open Sub Menu   Networking   Logical Switches
    Navigate To Page          Logical Switches
    Click Link                Link=Create logical switch
    Dialog Should Be Visible  Create Logical Switch
    Dialog Button Should Be Visible  Close
    Click Button                     id=cic-torlogicalswitch-nolsgs-cancel
    Dialog Should Not Be Visible     Create Logical Switch

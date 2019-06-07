*** Settings ***
Documentation      Logical Switch Groups Page test suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout And Close Browser
Force Tags         smoke  logicalswitchgroups  c7000
Test Timeout     ${TEST_TIMEOUT}


*** Test Cases ***
'Create logical switch group' Dialog Elements Should Appear As Expected
    [Documentation]  Logical Switch Groups page Dialog 'Create logical switch group' Elements Should Appear As Expected
    ...    \n Navigate to Logical Switch Groups page
    ...    \n Click "Create Logical Switch Groups"
    ...    \n "Create  Logical Switch Group" Dialog box Should be visible
    ...    \n Verify text can be input into the name field Use random characters
    ...    \n Select Logical Switch Type from the "Logical Switch" list
    ...    \n "Create" button should be visible
    ...    \n "Create+" button should be visible
    ...    \n "Cancel" button should be visible
    ...    \n Click "Cancel" button in "Create Logical Switch Group" Dialog box
    ...    \n "Create Logical Switch" Dialog box Should not be visible

    Open Sub Menu   Networking   Logical Switch Groups
    Navigate To Page          Logical Switch Groups
    Click Link                Link=Create logical switch group
    Dialog Should Be Visible  Create Logical Switch Group

    ${lsg_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Wait for Element and Input Text    xpath=//input[@id='cic-torswitchgroup-add-name']  ${lsg_name}

    @{list_switch_types}=  Create List From Drop Down Menu  cic-torswitchgroup-add-switch-type
    Remove values From List  ${list_switch_types}  Choose one
    :For  ${switch_type}  In  @{list_switch_types}
    \    Select Item From Drop Down Menu  torswitchgroups.common.type  ${switch_type}
    \    Message Should Be Displayed To Confirm Element Selection  ${switch_type}
#    \    Iterate Through Number Of Switches

    Dialog Element Should Be Visible  xpath=//input[@id='cic-torswitchgroup-add']
    Dialog Element Should Be Visible  xpath=//input[@id='cic-torswitchgroup-again']
    Dialog Element Should Be Visible  xpath=//a[@id='cic-torswitchgroup-add-close']
    Click Element                     id=cic-torswitchgroup-add-close
    Dialog Should Not Be Visible      Create Logical Switch Group


*** Keywords ***
Iterate Through Number Of Switches
    [Documentation]  Selecting Number of Switches for each Logical Switch Type
    ${list_of_switches}=  Create List From Drop Down Menu   cic-torswitchgroup-add-switch-number-value
    :For  ${no_of_switches}  In  @{list_of_switches}  # Removing default value
    \    Select Item From Drop Down Menu  torswitchgroups.common.number  ${no_of_switches}

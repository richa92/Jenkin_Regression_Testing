*** Settings ***
Documentation      Racks Page Test Suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout and Close Browser
Force Tags         smoke  racks
Test Timeout       ${TEST_TIMEOUT}


*** Test Cases ***
'Add Rack' Dialog Elements Should Appear As Expected
    [Tags]  c7000  tbird
    [Documentation]  Racks Page dialog 'Add Rack' Elements Should Appear As Expected
    ...   \n Navigate to "Racks" page
    ...   \n Click Actions
    ...   \n Click "Add"
    ...   \n "Add Rack" Dialog box should be visible
    ...   \n Iterate through items in panel selection menu
    ...   \n Enter text into Name field (use random characters)
    ...   \n Add button should be visible and primary in "Add Rack" Dialog box
    ...   \n Add+ button should be visible in "Add Rack" Dialog box
    ...   \n Click Cancel button in "Add Rack" Dialog box
    ...   \n "Add Rack" Dialog box should not be visible

    Open Sub Menu   Facilities   Racks
    Navigate to Page          Racks
    Click Link                Link=Add rack
    Dialog Should Be Visible  Add Rack
    ${racks_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text      id=cic-rack-details-name  ${racks_name}
    ${panels}=    Create List From Action or Panel Drop Menu  cic-rack-add-panel-selector
    :FOR  ${panel}  in  @{panels}
    \    Select Dialog Panel          cic-rack-add-panel-selector  ${panel}
    Dialog Element Should Be Visible  css=#cic-rack-add.hp-primary
    Dialog Element Should Be Visible  id=cic-rack-addplus
    Click Element                     id=cic-rack-cancel
    Dialog Should Not Be Visible      Add Rack

'Edit Rack' Dialog Elements Should Appear As Expected
    [Tags]  c7000
    [Documentation]  Racks Page dialog 'Edit Rack' Elements Should Appear As Expected
    ...   \n Navigate to "Racks" page
    ...   \n Navigate to "Racks" page
    ...   \n Click Actions
    ...   \n Click "Edit"
    ...   \n "Edit Rack" Dialog box should be visible
    ...   \n Iterate through items in panel selection menu
    ...   \n Enter text into Name field (use random characters)
    ...   \n OK button should be visible and primary in "Edit Rack" Dialog box
    ...   \n Click Cancel button in "Edit Rack" Dialog box
    ...   \n "Edit Rack" Dialog box should not be visible

    Navigate to Page  Racks
    Randomly Select Rack
    Select Item From Action or Panel Drop Menu  cic-rack-actions  Edit
    Element Should Be Visible  xpath=//section[@id='cic-rack-edit-section']//h1[span[text()='Edit']]
    ${racks_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-rack-details-name  ${racks_name}
    ${panels}=  Create List From Action or Panel Drop Menu  cic-rack-edit-panel-selector
    :FOR  ${panel}  in  @{panels}
    \  Select Dialog Panel  cic-rack-edit-panel-selector  ${panel}
    Dialog Element Should Be Visible  css=#cic-rack-update.hp-primary
    Click Element  id=cic-rack-cancel
    Dialog Element Should Not Be Visible  xpath=//section[@id='cic-rack-edit-section']//h1[span[text()='Edit']]

'Remove Rack' Dialog Elements Should Appear As Expected
    [Tags]  tbird  c7000
    [Documentation]  Racks Page dialog 'Remove Rack' Elements Should Appear As Expected
    ...   \n Navigate to "Racks" page
    ...   \n Navigate to "Racks" page
    ...   \n Click Actions
    ...   \n Click "Remove"
    ...   \n "Remove Rack" Dialog box should be visible
    ...   \n "Yes, remove" button should be visible and primary in "Remove Rack" Dialog box
    ...   \n Click Cancel button in "Remove Rack" Dialog box
    ...   \n "Remove Rack" Dialog box should not be visible

    Navigate to Page             Racks
    Randomly Select Rack
    Select Item From Action or Panel Drop Menu  cic-rack-actions  Remove
    Dialog Should Be Visible          Remove
    Dialog Element Should Be Visible  css=.hp-notify
    Dialog Button Should Be Visible   Yes, remove
    Click Element                     xpath=//button[@class='hp-cancel' and text()='Cancel']
    Dialog Should Not Be Visible      Remove

*** Keywords ***
Randomly Select Rack
    [Documentation]    Select a rack from the list randomly
    ${rack_list}=   Get Items From Table
    ${rack_len}=  Get Length  ${rack_list}
    Pass Execution If   ${rack_len}==0    No racks found. Passing test since no more actions are available.
    ${rack}=    Select list Item Randomly  ${rack_list}
    Select Item From Table and Verify Element Visible  item=${rack}  element=cic-rack-details-title
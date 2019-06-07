*** Settings ***
Documentation      Data Center Page Test Suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout and Close Browser
Force Tags         smoke  datacenter  tbird  c7000
Test Timeout       ${TEST_TIMEOUT}


*** Test Cases ***
'Add' Dialog Elements Should Appear As Expected
    [Documentation]  Data Center Page dialog 'Add' Elements Should Appear As Expected
    ...   \n Navigate to Data Centers page
    ...   \n Click Actions menu
    ...   \n Click "Add"
    ...   \n "Add Data Centers" Dialog box Should be visible
    ...   \n Verify text can be input into the name field in "Add Data Centers" Dialog box
    ...   \n Iterate through items in panel selection menu
    ...   \n Add button should be visible and primary in "Add Data Centers" Dialog box
    ...   \n Add+ button should be visible in "Add Data Centers" Dialog box
    ...   \n Click Cancel button in "Add Data Centers" Dialog box
    ...   \n "Add Data Centers" Dialog box should not be visible

    Open Sub Menu   Facilities   Data Centers
    Navigate to Page  Data Centers
    Select Item From Action or Panel Drop Menu  cic-datacenter-actions  Add
    Dialog Should Be Visible  Add Data Center
    ${panels}=  Create List From Action or Panel Drop Menu  cic-datacenter-panel-selector
    :FOR  ${panel}  in  @{panels}
    \    Select Dialog Panel          cic-datacenter-panel-selector  ${panel}
    ${datacenter_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text                        id=cic-datacenter-name  ${datacenter_name}
    Dialog Element Should Be Visible  css=#cic-datacenter-add.hp-primary
    Dialog Element Should Be Visible  id=cic-datacenter-addplus
    Click Element                     id=cic-datacenter-add-cancel
    Dialog Should Not Be Visible      Add Data Center


'Edit' Dialog Elements Should Appear As Expected
    [Documentation]  Data Center Page dialog 'Edit' Elements Should Appear As Expected
    ...   \n Navigate to Data Centers page
    ...   \n Click Actions menu
    ...   \n Click "Edit"
    ...   \n "Edit Data Centers" Dialog box Should be visible
    ...   \n Iterate through items in panel selection menu
    ...   \n OK button should be visible and primary in "Edit Data Centers" Dialog box
    ...   \n Click Cancel button in "Edit Data Centers" Dialog box
    ...   \n "Edit Data Centers" Dialog box should not be visible

    Navigate to Page  Data Centers
    Select Item From Action or Panel Drop Menu  cic-datacenter-actions  Edit
    Dialog Should Be Visible     Edit
    ${panels}=  Create List From Action or Panel Drop Menu  cic-datacenter-panel-selector
    :FOR  ${panel}  in  @{panels}
    \    Select Dialog Panel  cic-datacenter-panel-selector  ${panel}
    ${datacenter_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text                        id=cic-datacenter-name  ${datacenter_name}
    Dialog Element Should Be Visible  css=#cic-datacenter-update.hp-primary
    Click Element                     id=cic-datacenter-edit-cancel
    Dialog Should Not Be Visible      Yes, proceed
    Click Element                     id=hp-form-navigate-away-proceed
    Dialog Should Not Be Visible  Edit

'Remove' Dialog Elements Should Appear As Expected
    [Documentation]  Data Center Page dialog 'Remove' Elements Should Appear As Expected
    ...   \n Navigate to Data Centers page
    ...   \n Click Actions menu
    ...   \n Click "Remove"
    ...   \n "Remove Data Centers" Dialog box should be visible
    ...   \n "Yes, remove" button should be visible and primary in "Remove" Dialog box
    ...   \n Click Cancel button in "Remove" Dialog box
    ...   \n "Remove Data Center" Dialog box should not be visible

    Navigate to Page                    Data Centers
    Select Item From Action or Panel Drop Menu  cic-datacenter-actions  Remove
    Dialog Should Be Visible          Remove
    Dialog Element Should Be Visible  css=.hp-notify
    Dialog Button Should Be Visible   Yes, remove
    Click Element                     css=.hp-cancel
    Dialog Should Not Be Visible      Remove

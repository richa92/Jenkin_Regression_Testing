***Settings***
Documentation       Enclosure Page Test Suite
Resource            ../resource.txt
Suite Setup         Suite Setup
Suite Teardown      Logout And Close Browser
Force Tags          smoke  enclosure
Test Timeout        ${TEST_TIMEOUT}

*** Variables***
${hostname_or_ip}    hponeview@hpe.net

***Test Cases***
C7000 Appliance 'Add Enclosure' Dialog Elements Should Appear As Expected
    [Tags]  c7000
    [Documentation]  c7000 Enclosure Page 'Add Enclosure' Dialog Should Dispaly Elements As Expected
    ...   \n Navigate to Enclosures Page
    ...   \n Click link "Add enclosure"
    ...   \n Dialog with title "Add Enclosure" should be visible
    ...   \n Hostname field should accept host name and ipv4 address
    ...   \n Select Each Radio Action item and validate sub elements
    ...   \n Iterate through items in panel selection menu
    ...   \n Enter text into Enclosure group Name field (use random characters)
    ...   \n Select License Radio Button
    ...   \n "Add" button should be visible/primary
    ...   \n "Add+" button should be visible
    ...   \n Click Cancel
    ...   \n Dialog should not be visible

    Open Sub Menu   Servers   Enclosures
    Navigate To Page  Enclosures
    Click Link  link=Add enclosure
    Dialog Should Be Visible  Add Enclosure
    Input Text  id=cic-enclosure-hostname  ${hostname_or_ip}

    # Select "Add enclosure for management" Radio button in "Add enclosure" dialog box
    Click Element  xpath=//div[@id='cic-enclosure-addas-radio']//input[@type='radio' and @value='Managed']
    Iterate Dialog Panel List Items  cic-enclosures-panel-selector
    ${enclosuregroup_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-enclosure-new-group  ${enclosuregroup_name}
    Click Element  id=cic-enclosure-licensing-oneview-advanced
    Dialog Element Should Be Visible  css=#cic-enclosure-add.hp-primary
    Dialog Element Should Be Visible  id=cic-enclosure-addplus
    Dialog Element Should Be Visible  id=cic-enclosure-add-cancel

    # Select "Add enclosure for monitoring" Radio button in "Add enclosure" dialog box
    Click Element   xpath=//div[@id='cic-enclosure-addas-radio']//input[@type='radio' and @value='Monitored']
    Iterate Dialog Panel List Items  cic-enclosures-panel-selector
    Dialog Element Should Be Visible  css=#cic-enclosure-add.hp-primary
    Dialog Element Should Be Visible  id=cic-enclosure-addplus
    Dialog Element Should Be Visible  id=cic-enclosure-add-cancel

    # Select "Add enclosure and migrate Virtual Connect domain" Radio button in "Add enclosure" dialog box
    Click Element  xpath=//div[@id='cic-enclosure-addas-radio']//input[@type='radio' and @value='Migrated']
    Iterate Dialog Panel List Items  cic-enclosures-panel-selector
    ${enclosuregroup_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-enclosure-new-group  ${enclosuregroup_name}
    Click Element  id=cic-enclosure-licensing-oneview-advanced
    Dialog Element Should Be Visible  id=cic-enclosure-add
    Dialog Element Should Be Visible  id=cic-enclosure-addplus
    Click Element  id=cic-enclosure-add-cancel
    Dialog Should Not Be Visible  Add Enclosure

Edit Enclosure Dialog Elements Should Appear As Expected
    [Tags]  tbird
    [Documentation]  Tbird Enclosure page Dialog 'Edit Enclosure' Should Display Elements As Expected
    ...   \n Navigate to Enclosures Page
    ...   \n Select an enclosure from the list
    ...   \n Click "Actions" menu.
    ...   \n Click "Edit"
    ...   \n Dialog with title "Edit <Enclosure Name>" should be visible
    ...   \n Enclosure name field should contain correct enclosure name
    ...   \n OK button should be visible and should be primary
    ...   \n Click Cancel
    ...   \n Dialog should not be visible

    Open Sub Menu   Servers   Enclosures
    Navigate To Page  Enclosures
    ${enclosure}=  Get Enclosure From Enclosures Table
    Select Item From Table and Verify Element Visible  ${enclosure}  cic-enclosure-details-title
    Click Element              css=div#cic-enclosure-actions>label
    Click Element              id=cic-enclosure-edit-action
    Element Should Be Visible  xpath=//section[@id='cic-enclosure-edit']/header/h1//span[text()='${enclosure}']
    Element Should Be Visible  css=input#cic-enclosure-update.hp-primary
    Click Element              id=cic-enclosure-edit-cancel
    Dialog Element Should Not Be Visible  xpath=//section[@id='cic-enclosure-edit']/header/h1//span[text()='${enclosure}']

Reset Enclosure Dialog Elements Should Appear As Expected
    [Tags]  tbird
    [Documentation]  Tbird Enclosure page Dialog 'Reset Enclosure' Should Display Elements As Expected
    ...   \n Navigate to Enclosures Page
    ...   \n Select an enclosure from the list
    ...   \n Click "Actions" menu
    ...   \n Click "Reset link module"
    ...   \n Dialog "Reset link module" should be visible
    ...   \n For each radio button
    ...     Click link module radio button
    ...     Radio button should be selected
    ...   \n "Yes, reset" button should be visible/primary
    ...   \n Click cancel button
    ...   \n Dialog "reset link module" should not be visible

    Navigate To Page  Enclosures
    ${enclosure}=  Get Enclosure From Enclosures Table
    Select Item From Table and Verify Element Visible  ${enclosure}  cic-enclosure-details-title
    Select Item From Action or Panel Drop Menu  cic-enclosure-actions  Reset link module
    Dialog Should Be Visible          Reset link module
    Click Element                     id=cic-enclosure-reset-em-radio-2
    Dialog Element Should Be Visible  css=#cic-enclosure-reset-em-ok.hp-primary
    Click Element                     id=cic-enclosure-reset-em-cancel
    Dialog Should Not Be Visible      Reset link module

Remove Enclosure Dialog Elements Should Appear As Expected
    [Tags]  tbird
    [Documentation]  Tbird Enclosure page Dialog 'Remove Enclosure' Should Display Elements As Expected
    ...   \n Navigate to Enclosures Page
    ...   \n Select an enclosure from the list
    ...   \n Click "Actions" menu
    ...   \n Click "Remove"
    ...   \n "Remove <enclosure name" dialog should be visible
    ...   \n "Yes, remove" button should be visible/primary
    ...   \n Click Cancel button
    ...   \n "Remove <enclosure name>" dialog should not be visible

    Navigate To Page  Enclosures
    ${enclosure}=  Get Enclosure From Enclosures Table
    Select Item From Table and Verify Element Visible  ${enclosure}  cic-enclosure-details-title
    Select Item From Action or Panel Drop Menu  cic-enclosure-actions  Remove
    Dialog Should Be Visible          Remove
    ${managed_by_le}=  Is Element Visible    xpath=//div[@class='hp-notify']//*[contains(text(), 'Unable to remove an enclosure')]
    Run Keyword If  '${managed_by_le}' != 'True'    Dialog Element Should Be Visible  css=.hp-button.hp-ok.hp-primary
    Click Element                     css=.hp-cancel[data-localize='core.common.cancel']
    Dialog Should Not Be Visible      Remove


*** Keywords ***
Get Enclosure From Enclosures Table
    [Documentation]  Get enclosure randomly from enclosure table and return
    ${enclosures}=   Get Items From Table
    ${enclosure}=    Select list Item Randomly  ${enclosures}
    [Return]         ${enclosure}

Iterate Dialog Panel List Items
    [Documentation]  Iterate Dialog Panel List Items
    [Arguments]      ${element}
    ${panels}=  Create List From Action or Panel Drop Menu  ${element}
    :FOR  ${panel}  in  @{panels}
    \    Select Item From Action or Panel Drop Menu  ${element}  ${panel}
    \    Panel Should Be Visible  ${panel}

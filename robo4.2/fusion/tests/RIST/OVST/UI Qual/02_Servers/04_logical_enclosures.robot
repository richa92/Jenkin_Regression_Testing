*** Settings ***
Documentation     Logical Enclosure page test suite
Resource          ../resource.txt
Suite Setup       Suite Setup
Suite Teardown    Logout And Close Browser
Force Tags        smoke  le  tbird
Test Timeout      ${TEST_TIMEOUT}

*** Test Cases ***
'Create Logical Enclosure' Dialog Elements Should Appear As Expected
    [Documentation]  Logical Enclosure page Dialog 'Create Logical Enclosure' Should Display Elements As Expected
    ...  \n Navigate to Logical Enclosure Page
   ...   \n Click "Create Logical Enclosure"
   ...   \n Create Logical Enclosure Dialog Should be visible
   ...   \n Verify text can be input into the name field, Use random characters
   ...   \n Select enclosures from the "Enclosures" list
   ...   \n Ensure Firmware pane is displayed along with "Manage Manually" button
   ...   \n Create button should be visible and should be primary
   ...   \n Create+ button should be visible
   ...   \n Click cancel button
   ...   \n "Create Logical Enclosure" dialog should not be visible

    Open Sub Menu   Servers   Logical Enclosures
    Navigate To Page          Logical Enclosures
    Click Link                link=Create logical enclosure
    Dialog Should Be Visible  Create Logical Enclosure
    ${lig_name} =    Generate Random String  8  chars=[LETTERS][NUMBERS]
    Wait for Element and Input Text                id=cic-logical-enclosure-name  ${lig_name}
    Click Element             css=li#logicalenclosures-add-enclosure-block div.hp-search-combo-control
    Element Should Be Visible  css=div.hp-search-combo-spacer > div.hp-search-combo-menu
    Dialog Element Should Be Visible  css=#cic-logical-enclosure-add.hp-primary
    Dialog Element Should Be Visible  id=cic-logical-enclosure-addplus
    Click Element                     id=cic-logical-enclosure-add-cancel
    Dialog Should Not Be Visible      Create logical enclosure

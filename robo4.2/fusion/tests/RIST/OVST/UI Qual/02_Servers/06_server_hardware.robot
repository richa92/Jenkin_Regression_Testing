***Settings***
Documentation      Oneview Server Hardware Validation
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout And Close Browser
Force Tags         smoke  serverhardware
Test Timeout       ${TEST_TIMEOUT}


*** Variables***
${hostname_or_ip}   hponeview@hpe.net

***Test Cases ***
'Add Server Hardware' Dialog Elements Should Appear as Expected
    [Tags]  c7000
    [Documentation]  Add Server Hardware page 'Add Server Hardware' Dialog Elements Should Appear as Expected
    ...   \n Navigate to Server Hardware Page
    ...   \n Click link 'Add Server Hardware'
    ...   \n 'Add Server Hardware' Dialog should be visible
    ...   \n Enter iLO IP address or hostname in input field should accept
    ...   \n Select Each Radio Button of Add server hardware
    ...   \n Ensure Credentials and general pane's are visible
    ...   \n Select Each License Radio Button
    ...   \n "Add" button should be visible/primary
    ...   \n "Add+" button should be visible
    ...   \n Click Cancel
    ...   \n 'Add Server Hardware' Dialog should not be visible

    Open Sub Menu   Servers   Server Hardware
    Navigate To Page  Server Hardware
    Click Link  link=Add server hardware
    Dialog Should Be Visible  Add Server Hardware
    Input Text  id=cic-server-hostname  ${hostname_or_ip}
    Click Element  id=cic-server-management-type-managed
    Element Should Be Visible  id=cic-server-credential-fs
    Element Should Be Visible  id=cic-server-general-fs
    Click Element   id=cic-server-licensing-oneview-noilo
    Element Should Be Visible  css=#cic-server-add.hp-primary
    Element Should Be Visible  id=cic-server-add-again
    Click Element   id=cic-server-add-cancel
    Dialog Should Not Be Visible  Add Server Hardware

'Launch Console' Dialog Elements Should Appear as Expected
    [Tags]  tbird
    [Documentation]  Server Hardware page 'Launch Console' Dialog Elements Should Appear as Expected
    ...   \n Navigate to Server Hardware Page
    ...   \n Select a server
    ...   \n Click Actions
    ...   \n Click "Launch Console"
    ...   \n Dialog should be visible
    ...   \n "Install software" button should be visible
    ...   \n "Already installed" button should be visible
    ...   \n Click Cancel button
    ...   \n Dialog should not be visible

    Open Sub Menu   Servers   Server Hardware
    Navigate To Page  Server Hardware
    ${server}=  Get Server From Servers Table
    Select Item From Table and Verify Element Visible  ${server}  cic-server-details-title
    Select Item From Action or Panel Drop Menu   cic-server-actions  Launch console
    Element Should Be Visible  id=cic-dialog-body
    Element Should Be Visible  id=cic-dialog-installer-button
    Element Should Be Visible  id=cic-dialog-already-installed-button
    Click Element              id=cic-dialog-cancel-button
    Dialog Element Should Not Be Visible  id=cic-dialog-body

'PowerOff' Dialog Elements Should Appear as Expected
    [Tags]  tbird
    [Documentation]  Server Hardware page 'PowerOff' Dialog Elements Should Appear as Expected
    ...   \n Navigate to Server Hardware Page
    ...   \n Select a server
    ...   \n Click Actions
    ...   \n Click "Power off"
    ...   \n "Power off <Server>" dialog should be visible
    ...   \n Momentary press button should be visible
    ...   \n Press and hold button should be visible
    ...   \n Click "Close"
    ...   \n "Power off <Server>" dialog should not be visible

    Navigate To Page  Server Hardware
    ${server}=  Get Server From Servers Table
    Select Item From Table and Verify Element Visible  ${server}  cic-server-details-title
    Set Selenium Implicit Wait  5s
    ${state}=  Is Element Visible    xpath=//div[@id='cic-interconnect-details-interconnect-power' and text()='On']
    Set Selenium Implicit Wait  ${SELENIUM_IMPLICIT_WAIT}
    Run Keyword If    ${state}==True    Power Off Dialog Should Open Correctly

'Reset' Dialog Elements Should Appear as Expected
    [Tags]  tbird
    [Documentation]  Server Hardware page 'Reset' Dialog Elements Should Appear as Expected
    ...   \n Navigate to Server Hardware Page
    ...   \n Select a server
    ...   \n Click Actions
    ...   \n Click "Reset"
    ...   \n "Reset <Server>" dialog should be visible
    ...   \n Reset button should be visible
    ...   \n Cold boot should be visible
    ...   \n Click "Cancel"
    ...   \n "Reset <Server>" dialog should not be visible

    Navigate To Page  Server Hardware
    ${server}=  Get Server From Servers Table
    Select Item From Table and Verify Element Visible  ${server}  cic-server-details-title
    ${server}=  Get Server From Servers Table
    Select Item From Table and Verify Element Visible  ${server}  cic-server-details-title
    Set Selenium Implicit Wait  5s
    ${state}=  Is Element Visible    xpath=//div[@id='cic-interconnect-details-interconnect-power' and text()='On']
    Set Selenium Implicit Wait  ${SELENIUM_IMPLICIT_WAIT}
    Run Keyword If    ${state}==True    Reset Dialog Should Open Correctly


'Reset ILO' Dialog Elements Should Appear as Expected
    [Tags]  tbird
    [Documentation]  Server Hardware 'Reset ILO' Dialog Elements Should Appear as Expected
    ...   \n Navigate to Server Hardware Page
    ...   \n Select a server
    ...   \n Click Actions
    ...   \n Click "Reset iLO"
    ...   \n "Reset iLO <Server>" dialog should be visible
    ...   \n Yes, reset button should be visible/primary
    ...   \n Click "Cancel"
    ...   \n "Reset iLO <Server>" dialog should not be visible

    Navigate To Page  Server Hardware
    ${server}=  Get Server From Servers Table
    Select Item From Table and Verify Element Visible  ${server}  cic-server-details-title
    Select Item From Action or Panel Drop Menu  cic-server-actions  Reset iLO
    Dialog Should Be Visible   Reset iLO
    Element Should Be Visible  css=#cic-server-softReset-confirm-yes.hp-primary
    Click Element              id=cic-server-softReset-cancel
    Dialog Should Not Be Visible  Reset iLO

*** Keywords ***
Get Server From Servers Table
    [Documentation]  Get server randomly from servers table and return
    ${servers}=   Get Items From Table
    ${server}=  Select list Item Randomly  ${servers}
    [Return]  ${server}

Power Off Dialog Should Open Correctly
    [Documentation]  The power off dialog should be displayed
    Select Item From Action or Panel Drop Menu  cic-server-actions  Power off
    Dialog Should Be Visible  Power off
    Dialog Button Should Be Visible  Momentary press
    Dialog Button Should Be Visible  Press and hold
    Click Element                    id=cic-server-poweroff-cancel
    Dialog Should Not Be Visible     Power off

Reset Dialog Should Open Correctly
    [Documentation]  Reset server dialog should be displayed
    Select Item From Action or Panel Drop Menu  cic-server-actions  Reset
    Dialog Should Be Visible         Reset
    Dialog Button Should Be Visible  Reset
    Dialog Button Should Be Visible  Cold boot
    Click Element                    id=cic-server-reset-cancel
    Dialog Should Not Be Visible     Reset

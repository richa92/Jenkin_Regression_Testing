***Settings***
Documentation    Interconnects Page Test Suite
Resource         ../resource.txt
Suite Setup      Suite Setup
Suite Teardown   Logout And Close Browser
Force Tags       smoke  interconnects  tbird
Test Timeout     ${TEST_TIMEOUT}


***Test Cases ***
'Power off' Dialog Elements Should Appear as Expected
    [Documentation]  Interconnects Page Dialog 'Power off' Elements Should Appear as Expected
    ...   \n Navigate to Interconnects page
    ...   \n Click Actions menu
    ...   \n Click "Power off"
    ...   \n "Power off" Dialog box Should be visible
    ...   \n "Yes, Power off" button should be visible and as primary in  "Power off" Dialog box
    ...   \n Click Cancel button in "Power off" Dialog box
    ...   \n "Power off" Dialog box should not be visible

    Open Sub Menu   Networking   Interconnects
    Navigate To Page             Interconnects
    Randomly Select Interconnect
    ${state}=  Get Text    xpath=//div[@id='cic-interconnect-details-interconnect-power']
    Run Keyword If  '${state}'=='On'    Power Off Dialog Should Open Correctly

'Reset' Dialog Elements Should Appear as Expected
    [Documentation]  Interconnects Page Dialog 'Reset' Elements Should Appear as Expected
    ...   \n Navigate to Interconnects page
    ...   \n Click Actions menu
    ...   \n Click "Reset"
    ...   \n "Reset" Dialog box Should be visible
    ...   \n Soft reset button should be visible in "Reset" Dialog box
    ...   \n Hard reset button should be visible in "Reset" Dialog box
    ...   \n Click Cancel button in "Reset" Dialog box
    ...   \n "Reset" Dialog box should not be visible

    Navigate To Page                  Interconnects
    Randomly Select Interconnect
    Set Selenium Implicit Wait  5s
    ${sas}=  Is Element Visible    xpath=//div[@id='cic-interconnect-details-model' and contains(text(), 'SAS')]
    ${state}=  Get Text    xpath=//div[@id='cic-interconnect-details-interconnect-power']
    Pass Execution If  ${sas}!=True    Interconnect is not SAS. Skipping reset test.
    Pass Execution If  '${state}'=='Off'    Interconnect is powered off. Skipping reset test.
    Set Selenium Implicit Wait  ${SELENIUM_IMPLICIT_WAIT}
    Click Link In Action Menu    Reset
    Dialog Should Be Visible          Reset
    Run Keyword If  ${sas}==True    Dialog Element Should Be Visible   id=cic-interconnect-softReset
    Run Keyword If  ${sas}==True    Dialog Element Should Be Visible   id=cic-interconnect-hardReset
    Run Keyword If  ${sas}==False    Dialog Element Should Be Visible  id=cic-interconnection-action-dialog-yes
    Click Element                     css=div.hp-dialog button.hp-cancel
    Dialog Should Not Be Visible      Reset

*** Keywords ***
Randomly Select Interconnect
    [Documentation]    Select an interconnect from the list randomly
    Wait Until Page Contains Element      xpath=//table[contains(@class, hp-master-table)]/tbody/tr/td
    ${icm}=   Get Items From Table
    ${len}=  Get Length  {icm}
    Pass Execution If   ${len}==0    No interconnects found.  Skipping test.
    ${icm}=    Select list Item Randomly  ${icm}
    Select Item From Table and Verify Element Visible  item=${icm}  element=cic-interconnect-details-title

Click Link In Action Menu
    [Documentation]   Click a link in the action menu
    [Arguments]    ${link}
    Click Element    xpath=//div[contains(@id, 'cic-interconnect-actions') and not(contains(@style, 'display: none'))]
    Click Element    xpath=//div[contains(@id, 'cic-interconnect-actions') and not(contains(@style, 'display: none'))]//a[text()='${link}']

Power Off Dialog Should Open Correctly
    [Documentation]  The power off dialog should be displayed
    Select Item From Action or Panel Drop Menu  cic-interconnect-actions  Power off
    Dialog Should Be Visible          Power off
    Dialog Element Should Be Visible  xpath=//button[contains(@class, 'hp-primary') and text()='Yes, power off']
    Click Element                     css=div.hp-dialog button.hp-cancel
    Dialog Should Not Be Visible      Power off

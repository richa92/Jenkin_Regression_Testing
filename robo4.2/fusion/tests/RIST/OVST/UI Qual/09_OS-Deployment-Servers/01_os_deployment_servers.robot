***Settings***
Documentation      OS Deployment Servers Page Test Suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout And Close Browser
Force Tags         smoke  osdeploymentservers  tbird
Test Timeout       ${TEST_TIMEOUT}

***Test Cases ***
Dialog 'Add OS Deployment Server' Elements Should Appear as Expected
    [Documentation]  OS Deployment Servers Page dialog 'Add OS Deployment Server' Elements Should Appear as Expected
    ...   \n OS Deployment Servers Validating Enclosure
    ...   \n Navigate to OS Deployment Servers Page
    ...   \n Click link 'OS Deployment Servers'
    ...   \n 'OS Deployment Servers' Dialog should be visible
    ...   \n Ensure General and Management Settings pane's are visible
    ...   \n Verify text can be input into the OS Deployment Servers name field
    ...   \n Enter text into Description field (use random characters)
    ...   \n Iterate through Deployment appliance list items
    ...   \n "Add" button should be visible/primary
    ...   \n Click Cancel
    ...   \n 'OS Deployment Servers' Dialog should not be visible

    Open Sub Menu   Appliance   OS Deployment Servers
    Navigate To Page  OS Deployment Servers
    Click Link  link=Add OS deployment server
    Element Should Be Visible  xpath=//div[@id='hp-change-page-container']//span[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='add os deployment server']
    Dialog Element Should Be Visible  id=cic-deploymentserver-add-general
    Dialog Element Should Be Visible  id=cic-deploymentserver-stackedpanel-remote
    ${osds_name}=   Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-deploymentserver-name  ${osds_name}
    ${osdes_name}=  Generate Random String  60  chars=[LETTERS][NUMBERS]
    Input Text  id=cic-deploymentserver-description  ${osdes_name}
    Dialog Element Should Be Visible  css=#cic-deploymentserver-add.hp-primary
    Click Element  id=cic-deploymentserver-add-cancel
    # If a confirmation dialog appears, click the proceed button
    #Set Selenium Implicit Wait      0.5
    #${dialog}=  Is Element Visible  id=hp-form-navigate-away-dialog
    #Set Selenium Implicit Wait  ${SELENIUM_IMPLICIT_WAIT}
    #Run Keyword If    ${dialog}==True    Click Element    id=hp-form-navigate-away-dialog
    Dialog Should Not Be Visible  OS Deployment Servers


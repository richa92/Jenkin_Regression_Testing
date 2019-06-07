***Settings***
Documentation      Server Hardware Types Page Test Suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout And Close Browser
Force Tags         smoke  serverhardwaretypes  tbird
Test Timeout     ${TEST_TIMEOUT}


***Test Cases ***
'Edit' Dialog Elements Should Appear as Expected
    [Documentation]  Server Hardware Types Page 'Edit' Dialog Should Display Elements As Expected
    ...   \n Navigate to Server Hardware Types page
    ...   \n Select server hardware (random?)
    ...   \n Click actions
    ...   \n Click edit
    ...   \n "Edit <Server Hardware>" dialog should be visible
    ...   \n OK button should be visible/primary
    ...   \n Click cancel button
    ...   \n "Edit <Server Hardware>" dialog should not be visible

    Open Sub Menu   Servers   Server Hardware Types
    Navigate To Page          Server Hardware Types
    Log     Getting count of items in server hardware list    console=True
    ${item_count}=    Get Text    //div[@class='hp-page-resource-info']//span[@class='hp-page-item-count']
    Log   Found ${item_count} items    console=True
    Run Keyword If  ${item_count} > 0  Select Item From List and Activate Edit Dialog

*** Keywords ***
Select Item From List and Activate Edit Dialog
    [Documentation]  Select an individual item from a list and click the edit button
    Click Element                 xpath=//div[@id='cic-servertypes-page']//ol[@class='hp-master-grid hp-active']/li[3]
    Select Item From Action or Panel Drop Menu  cic-servertypes-actions  Edit
    Dialog Should Be Visible      Edit
    Element Should Be Visible     css=#cic-servertypes-edit-ok.hp-primary
    Click Element                 id=cic-servertypes-edit-cancel
    Dialog Should Not Be Visible  Edit

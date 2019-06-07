*** Settings ***
Documentation      Unmanaged Devices Page Test Suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout and Close Browser
Force Tags         smoke  unmanageddevices  tbird  c7000
Test Timeout       ${TEST_TIMEOUT}

*** Test Cases ***
'Add' Dialog Elements Should Appear as Expected
    [Documentation]  Unmanaged Devices Page dialog 'Add' Elements Should Appear as Expected
    ...   \n Navigate to "Unmanaged Devices" page
    ...   \n Click "Unmanaged Devices"
    ...   \n "Add Unmanaged Devices" Dialog Should be visible
    ...   \n Verify text can be input into the name field in "Add Unmanaged Devices" Dialog box
    ...   \n Select Height value from the list
    ...   \n Add button should be visible and primary in "Add Unmanaged Devices" Dialog box
    ...   \n Add+ button should be visible in "Add Unmanaged Devices" Dialog box
    ...   \n Click Cancel button in "Add Unmanaged Devices" Dialog box
    ...   \n "Add Unmanaged Devices" Dialog box should not be visible

    Open Sub Menu   Facilities   Unmanaged Devices
    Navigate to Page                  Unmanaged Devices
    Click Link                        Link=Add unmanaged device
    ${random_name} =  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text                        id=cic-unmanaged-name  ${random_name}
    Dialog Should Be Visible          Add Unmanaged Device
    Dialog Element Should Be Visible  css=#cic-unmanaged-add.hp-primary
    Dialog Element Should Be Visible  id=cic-unmanaged-addplus
    Click Element                     id=cic-unmanaged-add-cancel
    Dialog Should Not Be Visible      Add Unmanaged Device

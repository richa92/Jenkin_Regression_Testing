*** Settings ***
Documentation      Users And Groups Page Test Suite
Resource           ../resource.txt
Suite Setup        Suite Setup
Suite Teardown     Logout and Close Browser
Force Tags         smoke  usersandgroups  tbird  c7000
Test Timeout       ${TEST_TIMEOUT}

*** Variables***
${email_charc}   Oneview@Mphasis.com

*** Test Cases ***
Dialog 'Add User' Elements Should Appear as Expected
    [Documentation]  Users And Groups Page dialog 'Add User' Elements Should Appear as Expected
    ...    \n Navigate to Users and Groups page
    ...    \n Click Actions
    ...    \n Click "Add User"
    ...    \n Add User Dialog should be visible
    ...    \n Enter text into Name field (use random characters)
    ...    \n Select each role from the drop down list
    ...    \n Click Scope for Specialized Role
    ...    \n Click "Add permission" button
    ...    \n Enter text into Email field (use random characters)
    ...    \n "Add" button should be visible/primary
    ...    \n "Add+" button should be visible
    ...    \n Click Cancel Button in Add User Dialog box
    ...    \n Add User Dialog should not be visible

    Open Sub Menu   Appliance   Users and Groups
    Navigate to Page  Users and Groups
    Select Item From Action or Panel Drop Menu  cic-user-actions  Add user
    Dialog Should Be Visible  Add User
    ${random_name}=  Generate Random String  8  chars=[LETTERS][NUMBERS]
    Input Text       id=fs-user-loginname  ${random_name}
    Click Element    xpath=//*[@id='fs-user-add-permission-datatable']/tbody/tr/td[1]//div[@class='hp-search-combo-control']

    ${role_list}=    Set Variable    //div[@class='hp-search-combo-menu']/ol[@class='hp-search-combo-scroller hp-options']/li/span
    ${count}=    Get Matching Xpath Count    ${role_list}
    ${role}=    Create List
    :FOR    ${i}    IN RANGE    1    ${count} + 1
    \    ${role}=    Get Text    xpath=(${role_list})[${i}]
    \    Click Element    xpath=//div[@class='hp-search-combo-menu']/ol[@class='hp-search-combo-scroller hp-options']/li/span[contains(text(),'${role}')]
    \    Click Element    xpath=//*[@id='fs-user-add-permission-datatable']/tbody/tr/td[1]//div[@class='hp-search-combo-control']

    Click Element    css=#fs-user-permission-scopeName1-input
    Click Element    //input[@id='fs-user-add-permission-button']
    Input Text                        id=fs-user-email  ${email_charc}
    Dialog Element Should Be Visible  css=#fs-user-add.hp-primary
    Dialog Element Should Be Visible  id=fs-user-add-again
    Click Element                     id=fs-user-add-cancel
    Dialog Should Not Be Visible      Add user

Dialog 'Edit User' Elements Should Appear as Expected
    [Documentation]  Users And Groups Page  dialog 'Edit User' Elements Should Appear as Expected
    ...    \n Navigate to Users and Groups page
    ...    \n Click Actions
    ...    \n Click "Edit"
    ...    \n Edit User Dialog should be visible
    ...    \n For each radio button
    ...      Click Specialized, Full and Read only radio button
    ...      Click the Check boxes for Specialized Role
    ...      Radio button should be selected
    ...    \n Enter text into Email field (use random characters)
    ...    \n "OK" button should be visible/primary
    ...    \n Click Cancel Button in Edit User Dialog box
    ...    \n Edit User Dialog should not be visible

    Navigate to Page                  Users and Groups
    Select Item From Action or Panel Drop Menu  cic-user-actions  Edit
    Dialog Element Should Be Visible  xpath=//section[@id='fs-user-edit-section']//h1[text()='Edit administrator']
    Input Text                        id=fs-user-edit-email  ${email_charc}
    Dialog Element Should Be Visible  css=#fs-user-edit.hp-primary
    Click Element                     id=fs-user-edit-cancel
    Dialog Should Not Be Visible      Edit administrator

Dialog 'Remove User' Elements Should Appear as Expected
    [Documentation]  Users And Groups Page dialog 'Remove User' Elements Should Appear as Expected
    ...    \n Navigate to Users and Groups page
    ...    \n Click Actions
    ...    \n Click "Remove"
    ...    \n Remove User Dialog should be visible
    ...    \n "Yes, remove" button should be visible/primary
    ...    \n Click Cancel Button in Remove User Dialog box
    ...    \n Remove User Dialog should not be visible

    Navigate to Page              Users and Groups
    Select Item From Action or Panel Drop Menu  cic-user-actions  Remove
    Dialog Should Be Visible      Unauthorized action
    Click Element                 css=#hp-body-div footer button
    Dialog Should Not Be Visible  Unauthorized action

Dialog 'Add Group' Elements Should Appear as Expected
    [Documentation]  Users And Groups Page dialog 'Add Group' Elements Should Appear as Expected
    ...    \n Navigate to Users and Groups page
    ...    \n Click Actions
    ...    \n Click "Add Group"
    ...    \n Add Group  Dialog should be visible
    ...    \n "Close" button should be visible/primary
    ...    \n Click Close Button in Add Group User Dialog box
    ...    \n Add Group User Dialog should not be visible

    Navigate to Page              Users and Groups
    Select Item From Action or Panel Drop Menu  cic-user-actions  Add group
    Dialog Should be Visible      Add Group
    Click Element                 xpath=//a[@class='hp-button hp-primary' and text()='Close']
    Dialog Should Not be Visible  Add Group

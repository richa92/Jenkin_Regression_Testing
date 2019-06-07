*** Settings ***
Documentation        OVF167 - n009_NonIA_Role_Group_CanNot_Create_Scope

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF167.txt


Variables            ${DATA_FILE}

Test Setup           Pre Condition    directoryProfiles=${directory}    groupProfiles=${n009_new_group_wo_scope_role}
Test Teardown        Clear Test Environment    directoryFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_n009_NonIA_Role_Group_CanNot_Create_Scope
    [Documentation]   n009_NonIA_Role_Group_CanNot_Create_Scope
    Log To Console    \n- Test Case: n009_NonIA_Role_Group_CanNot_Create_Scope
    credential Login     ${group_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{group_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Should Failed To Create Scope    body=${p005_scopes[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: n009_NonIA_Role_Group_CanNot_Create_Scope

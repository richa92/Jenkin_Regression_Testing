*** Settings ***
Documentation        OVF167 - n005_SO_Role_Group_CanNot_Delete_Scope

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

Test Setup           Pre Condition    directoryProfiles=${directory}    groupProfiles=${n004_so_role_only_group}    scopeProfiles=${p005_scopes}
Test Teardown        Clear Test Environment    directoryFlag=${true}   scopeFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_n005_SO_Role_Group_CanNot_Delete_Scope
    [Documentation]  n005_SO_Role_Group_CanNot_Delete_Scope
    Log To Console    \n- Test Case: n005_SO_Role_Group_CanNot_Delete_Scope
    credential Login     ${group_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{group_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Should Failed To Delete Scope
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: n005_SO_Role_Group_CanNot_Delete_Scope

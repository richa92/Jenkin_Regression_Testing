*** Settings ***
Documentation        OVF167 - p005_SA_Role_Group_Can_Create_Scope

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./OVF167_C7000.txt


Variables            ${DATA_FILE}

Test Setup           Pre Condition    directoryProfiles=${directory}    groupProfiles=${p003_new_group_with_sa_role}
Test Teardown        Clear Test Environment    directoryFlag=${true}    scopeFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_p005_SA_Role_Group_Can_Create_Scope
    [Documentation]   p005_SA_Role_Group_Can_Create_Scope
    Log To Console    \n- Test Case: p005_SA_Role_Group_Can_Create_Scope
    ${index} =    Set Variable    ${0}
    credential Login     ${group_credentials_list}
    :FOR     ${credential}     IN     @{group_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        ${ret} =    Create Scope    ${p005_scopes[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    \        Wait For Task2    ${ret}
    Log To Console    \n- Test Case: Successfully: p005_SA_Role_Group_Can_Create_Scope

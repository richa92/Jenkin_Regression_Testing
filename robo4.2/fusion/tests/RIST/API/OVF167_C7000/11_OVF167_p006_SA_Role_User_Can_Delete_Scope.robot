*** Settings ***
Documentation        OVF167 - p006_SA_Role_User_Can_Delete_Scope

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

Test Setup           Pre Condition    userProfiles=${p003_new_users_with_sa_role}  scopeProfiles=${p005_scopes}
Test Teardown        Clear Test Environment   userFlag=${true}    scopeFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_p006_SA_Role_User_Can_Delete_Scope
    [Documentation]   p006_SA_Role_User_Can_Delete_Scope
    Log To Console    \n- Test Case: p006_SA_Role_User_Can_Delete_Scope
    credential Login     ${user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Remove Scope By Name    ${p005_scopes[${index}]['name']}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: p006_SA_Role_User_Can_Delete_Scope

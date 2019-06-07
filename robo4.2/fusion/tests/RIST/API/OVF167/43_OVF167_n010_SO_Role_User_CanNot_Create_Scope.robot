*** Settings ***
Documentation        OVF167 - n010_SO_Role_User_CanNot_Create_Scope

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

Test Setup           Pre Condition    userProfiles=${n004_so_role_only_user}  scopeProfiles=${p005_scopes}
Test Teardown        Clear Test Environment   userFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_n010_SO_Role_User_CanNot_Create_Scope
    [Documentation]   n010_SO_Role_User_CanNot_Create_Scope
    Log To Console    \n- Test Case: n010_SO_Role_User_CanNot_Create_Scope
    credential Login     ${p003_user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{p003_user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Should Failed To Create Scope    body=${p005_scopes[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: n010_SO_Role_User_CanNot_Create_Scope

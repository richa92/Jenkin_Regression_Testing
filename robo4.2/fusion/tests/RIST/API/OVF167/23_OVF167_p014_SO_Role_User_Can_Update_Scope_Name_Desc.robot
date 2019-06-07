*** Settings ***
Documentation        OVF167 - p014_SO_Role_User_Can_Update_Scope_Name_Desc

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
Test Setup           Pre Condition    userProfiles=${n004_so_role_only_user}    scopeProfiles=${p005_scopes}
Test Teardown        Clear Test Environment   userFlag=${true}   scopeFlag=${true}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_p014_SO_Role_User_Can_Update_Scope_Name_Desc
    [Documentation]   p014_SO_Role_User_Can_Update_Scope_Name_Desc
    Log To Console    \n- Test Case: n008_SO_Role_User_CanNot_Update_Scope_Name_Desc
    credential Login     ${p003_user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{p003_user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Edit Scope Resources    scope_body=${p005_scopes[${index}]}    new_name=${p011_update_body[${index}]['name']}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: p014_SO_Role_User_Can_Update_Scope_Name_Desc

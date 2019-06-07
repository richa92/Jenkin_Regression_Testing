*** Settings ***
Documentation        OVF167 - p011_SA_Role_User_Can_Update_Scope_Name_Desc

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
Test Setup           Pre Condition    userProfiles=${p003_new_users_with_sa_role}    scopeProfiles=${p005_scopes}
Test Teardown        Clear Test Environment   userFlag=${true}   scopeFlag=${true}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_p011_SA_Role_User_Can_Update_Scope_Name_Desc
    [Documentation]   p011_SA_Role_User_Can_Update_Scope_Name_Desc
    Log To Console    \n- Test Case: p011_SA_Role_User_Can_Update_Scope_Name_Desc
    credential Login     ${p003_user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{p003_user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Edit Scope Resources    scope_body=${p005_scopes[${index}]}    new_name=${p011_update_body[${index}]['name']}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: p011_SA_Role_User_Can_Update_Scope_Name_Desc

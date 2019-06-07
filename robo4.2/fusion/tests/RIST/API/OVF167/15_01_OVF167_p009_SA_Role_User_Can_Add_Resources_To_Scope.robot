*** Settings ***
Documentation        OVF167 - p009_SA_Role_User_Can_Add_Resources_To_Scope

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
Test Setup           Pre Condition    userProfiles=${p003_new_users_with_sa_role}    scopeProfiles=${p005_scopes}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_p009_SA_Role_User_Can_Add_Resources_To_Scope
    [Documentation]   p009_SA_Role_User_Can_Add_Resources_To_Scope
    Log To Console    \n- Test Case: p009_SA_Role_User_Can_Add_Resources_To_Scope
    credential Login     ${user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Edit Scope Resources    ${p007_edit_body[${index}]}    ${true}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: p009_SA_Role_User_Can_Add_Resources_To_Scope

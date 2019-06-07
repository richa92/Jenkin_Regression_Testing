*** Settings ***
Documentation        OVF167 - p007_SO_Role_User_Can_Add_Resources_To_Scope

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
Test Setup           Pre Condition    userProfiles=${p001_new_users_with_so_role}    scopeProfiles=${p005_scopes}


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_p007_SO_Role_User_Can_Add_Resources_To_Scope
    [Documentation]   p007_SO_Role_User_Can_Add_Resources_To_Scope
    credential Login     ${user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Edit Scope Resources    ${p007_edit_body[${index}]}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: p007_SO_Role_User_Can_Add_Resources_To_Scope

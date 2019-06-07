*** Settings ***
Documentation        OVF167 - p013_SO_Role_Read_Only_User_Can_Get_Roles_Info

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
Test Setup           Pre Condition    userProfiles=${p001_new_users_with_so_role}
Test Teardown        Clear Test Environment   userFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
OVF167_p013_SO_Role_Read_Only_User_Can_Get_Roles_Info
    [Documentation]   p013_SO_Role_Read_Only_User_Can_Get_Roles_Info
    Log To Console    \n- Test Case: p013_SO_Role_Read_Only_User_Can_Get_Roles_Info
    credential Login     ${user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Get Role Info
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: p013_SO_Role_Read_Only_User_Can_Get_Roles_Info

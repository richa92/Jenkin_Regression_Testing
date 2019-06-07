*** Settings ***
Documentation        OVF167 - p008_SO_Role_User_Can_Remove_Resources_From_Scope

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

Test Teardown        Clear Test Environment   userFlag=${true}    scopeFlag=${true}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
OVF167_p008_SO_Role_User_Can_Remove_Resources_From_Scope
    [Documentation]   p008_SO_Role_User_Can_Remove_Resources_From_Scope
    Log To Console    \n- Test Case: p008_SO_Role_User_Can_Remove_Resources_From_Scope
    credential Login     ${user_credentials_list}
    ${index} =    Set Variable    ${0}
    :FOR     ${credential}     IN     @{user_credentials_list}
    \        Fusion Api Switch Active User      ${credential['userName']}
    \        Can Edit Scope Resources    ${p007_edit_body[${index}]}    ${false}
    \        ${index} =    Set Variable    ${index+1}
    Log To Console    \n- Test Case: Successfully: p008_SO_Role_User_Can_Remove_Resources_From_Scope User Can Not Delete Other Resources with sa role

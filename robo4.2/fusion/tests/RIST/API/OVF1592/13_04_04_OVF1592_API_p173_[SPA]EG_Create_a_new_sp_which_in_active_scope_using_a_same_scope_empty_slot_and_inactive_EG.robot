*** Settings ***
Documentation        Server Profiles Associated with EG_Create a new server profile which in active scope using a server hardware which in same scope, EG is in inactive scope
Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              copy
Library              Collections
Library              String
Library              json
Library              XML
Library              SSHLibrary
Library              Dialogs
Variables            ${DATA_FILE}
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Suite Setup           Run Keywords    Login Appliance  ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
...                   AND    Prepare Environment For Test
Suite Teardown        Clear Environment After Test   ${create_server_profile}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with EG Create a new sp which in active scope using a same scope empty slot and inactive EG
    [Documentation]  OVF1592 API p173 [SPA] Server Profiles Associated with EG Create a new sp which in active scope using a same scope empty slot and inactive EG
    Log   Create new server profiles sp5     console=True
    Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
    ${resp}=  Add Server Profile  ${create_server_profile_EG4}
    Wait For Task2   ${resp}  timeout=600
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}

*** Keywords ***
Prepare Environment For Test
    [Documentation]  Prepare Environment For Test
    Log   Add scope "Test" for Enc: CN75120D77    console=True
    ${resp}=  Patch Resources Scopes   ENC:${enc_name_list[1]}   ${Patch_add_Scope1}
    Wait For Task2   ${resp}   timeout=120
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${enc_name_list[1]}   ${True}

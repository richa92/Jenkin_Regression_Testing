*** Settings ***
Documentation         Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the inactive scope
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
Suite Teardown        Logout APpliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with Server hardware_Create a server profile which in active scope using a empty bay which in the different active scope
    [Documentation]  OVF1592_API_n162 [SPA] Server Profiles Associated with enclosure_Create a server profile which in active scope using a empty bay which in the different scope with new server profile
    Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
    Log   Create new server profiles sp5     console=True
    ${resps}=  Add Server Profile  ${create_server_profile_EG4}
    Wait For Task2   ${resps}   timeout=600    PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

*** Keywords ***
Prepare Environment For Test
    [Documentation]  Prepare Environment For Test
    Log   Add scope "Production" for Enc: CN75120D77    console=True
    ${resp}=  Patch Resources Scopes   ENC:${enc_name_list[1]}   ${Patch_remove_Scope0}
    Wait For Task2   ${resp}   timeout=120
    ${resp}=  Patch Resources Scopes   ENC:${enc_name_list[1]}   ${Patch_add_Scope0}
    Wait For Task2   ${resp}   timeout=120
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:${enc_name_list[1]}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${enc_name_list[1]}   ${False}

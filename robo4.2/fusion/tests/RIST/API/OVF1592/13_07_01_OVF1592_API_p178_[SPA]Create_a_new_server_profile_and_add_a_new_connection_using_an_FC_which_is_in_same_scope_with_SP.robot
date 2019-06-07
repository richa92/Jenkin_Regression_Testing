*** Settings ***
Documentation        Server Profiles Associated with FC Create a new server profile and add a new connection using an FC, the FC is in same scope with SP
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
...                   AND            Set LIG Uplinksets And Sync To LI  ${lig_fc_path}  ${li_update_dto}
Suite Teardown        Clear Environment After Test   ${create_sp_fc1}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with FC Create a new server profile and add a new connection using an FC, the FC is in same scope with SP
    [Documentation]  OVF1592 API p178 [Server Profile Administrator] Server Profiles Associated with FC Create a new server profile and add a new connection using an FC the FC is in same scope with SP
    Log     Create new server profiles sp5 with add fc2      console=True
    Active Permission Session    ${edit_spa_users_permission}    ${credentials['spa_credentials']}
    ${resp}=  Add Server Profile  ${create_sp_fc1}
    Wait For Task2   ${resp}   timeout=600
    Log   Check sp5 information   console=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}

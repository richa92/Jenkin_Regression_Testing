*** Settings ***
Documentation        Server Profiles Associated with network-Sets Create a new server profile and add a new connection using an network-Sets, the network-Sets is in same scope with SP
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
...                   AND            Prepare Environment For Test
Suite Teardown        Clear Environment After Test   ${create_sp_network1}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with network-Sets Create a new server profile and add a new connection using an network-Sets, the network-Sets is in same scope with SP
    [Documentation]  OVF1592 API p178 [Server Profile Administrator] Server Profiles Associated with network-Sets Create a new server profile and add a new connection using an network-Sets the network-Sets is in same scope with SP
    Log     Create new server profiles sp5 with add netset2      console=True
    Active Permission Session    ${edit_spa_users_permission}    ${credentials['spa_credentials']}
    ${resp}=  Add Server Profile  ${create_sp_netsets1}
    Wait For Task2   ${resp}   timeout=600
    Log   Check sp5 information   console=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}

*** Keywords ***
Prepare Environment For Test
    [Documentation]  Configure network-sets and Add network-Sets uplink-sets for testing
    Log    configure network-sets    console=True
    ${resps}=   Update Network Set    ${network_sets_for_sp}
    Wait For Task2   ${resps}   timeout=60

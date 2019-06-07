*** Settings ***
Documentation        Server Profiles supports SBAC Create new SP which is in the active scope
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


Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
Suite Teardown        Clear Environment After Test   ${create_server_profile}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles supports SBAC Create new SP which is in the active scope
    [Documentation]  OVF1592 API p163 [Server Profile Administrator] Server Profiles supports SBAC Create new SP which is in the active  scope

    Log    Create new server profiles sp5    console=True
    ${resps}=  Add Server Profile  ${create_server_profile}
    Wait For Task2   ${resps}  timeout=600
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SP:${new_sp_name}   ${False}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}

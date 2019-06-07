*** Settings ***
Documentation        Server Profiles Associated with EG_Create a new server profile which in active scope using unassigned server hardware, fill in an EG which in the active scope
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
Suite Teardown        Clear Environment After Test   ${create_server_profile_EG1}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with EG_Create a new server profile which in active scope using unassigned server hardware, fill in an EG which in the active scope
    [Documentation]  OVF1592 API p170 [Server Profile Administrator] Server Profiles Associated with EG_Create a new server profile which in active scope using unassigned server hardware, fill in an EG which in the active scope

    Log   Create new server profiles sp5     console=True
    ${resp}=  Add Server Profile  ${create_server_profile_EG1}
    Wait For Task2   ${resp}  timeout=600
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}

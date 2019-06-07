*** Settings ***
Documentation        Create a new server profile and select an existing volume which is in the same active scope with SP
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spa_credentials"]}
Test Teardown        Clear Environment After Test   ${create_server_profile_volume1}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Create a new server profile and select an existing volume which is in the same active scope with SP
    [Documentation]  OVF1592 API p190 [Server Profile Administrator] Create a new server profile and select an existing volume which is in the same active scope with SP
    Log     Create new server profiles sp5   console=True
    ${resp}=  Add Server Profile  ${create_server_profile_volume1}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait For Task2   ${resp}   timeout=600
    log   Check sp5 information   console=True
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}
    Validate Volume Assigned/Unassigned To Server Profile  ${vol_list[1]}  ${new_sp_name}  ${True}

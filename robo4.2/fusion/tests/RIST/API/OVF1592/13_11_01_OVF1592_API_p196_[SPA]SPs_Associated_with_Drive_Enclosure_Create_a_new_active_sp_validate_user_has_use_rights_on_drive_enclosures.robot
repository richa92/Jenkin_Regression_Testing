*** Settings ***
Documentation        SPA-Associated with Drive Enclosure_Create a new server profile, validate user has "use" rights on drive-enclosures category
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
Test Teardown        Clear Environment After Test   ${create_server_profile_de1}  Remove

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with Drive Enclosure Create a new active sp validate user has use rights on drive enclosures
    Log   Create new server profiles sp5 with active drive enclosure storage    console=True
    ${resp}=  Add Server Profile  ${create_server_profile_de1}
    Wait For Task2   ${resp}  timeout=20m  interval=10
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SP:${new_sp_name}   ${True}
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  DE:${drive_enc}   ${True}

*** Settings ***
Documentation        Associated with Drive Enclosure_Update a new server profile, validate user has "use" rights on drive-enclosures category
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
Test Teardown        Revert SP Environment After Test    ${Edit_sp_network_base}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with Drive Enclosure Update a new active sp validate user has use rights on drive enclosures
    Log   Update new server profiles sp2 with active drive enclosure storage    console=True
    ${resp}=  Edit Server Profile  ${Edit_server_profile_de1}
    Wait For Task2   ${resp}  timeout=20m  interval=10
    Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  DE:${drive_enc}   ${True}

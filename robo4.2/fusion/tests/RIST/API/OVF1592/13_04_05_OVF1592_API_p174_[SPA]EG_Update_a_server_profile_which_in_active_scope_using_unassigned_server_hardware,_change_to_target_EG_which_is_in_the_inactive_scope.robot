*** Settings ***
Documentation        Server Profiles Associated with EG_Update a server profile which in active scope using unassigned server hardware, change to target EG which is in the inactive scope
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
Test Teardown        Revert SP Environment After Test    ${Edit_server_profile_base}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with EG_Update a server profile which in active scope using unassigned server hardware, change to target EG which is in the inactive scope
    [Documentation]  OVF1592 API p174 [Server Profile Administrator] Server Profiles Associated with EG_Update a server profile which in active scope using unassigned server hardware, change to target EG which is in the inactive scope
    Log   Update SP2 TO EG-Synergy   console=True
    ${resp}=  Edit Server Profile     ${Edit_server_profile_EG1}
    Wait For Task2   ${resp}  timeout=600
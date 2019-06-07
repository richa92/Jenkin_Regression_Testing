*** Settings ***
Documentation        Server Profiles Associated with FCOE Update a server profile and edit the existing connection using FCOE, select a new FCOE which is in same scope with SP
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
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPA] - Server Profiles Associated with FCOE Update a server profile and edit the existing connection using FCOE, select a new FCOE which is in same scope with SP
    [Documentation]  OVF1592 API p180 [Server Profile Administrator] Server Profiles Associated with FCOE Update a server profile and edit the existing connection using FCOE, select a new FCOE which is in same scope with SP

    Log     Can be change server profiles sp2 from fcoe2 to fcoe1     console=True
    ${resp}=  Edit Server Profile  ${Edit_sp_fcoe4}
    Wait For Task2   ${resp}   timeout=600

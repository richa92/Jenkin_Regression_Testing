*** Settings ***
Documentation        Server Profiles Associated with network-Sets Update a server profile and add a new connection using an network-Sets, the network-Sets is in same scope with SP
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
[SPA] - Server Profiles Associated with network-Sets Update a server profile and add a new connection using an network-Sets, the network-Sets is in same scope with SP
    [Documentation]  OVF1592 API p179 [Server Profile Administrator] Server Profiles Associated with network-Sets Update a server profile and add a new connection using an network-Sets, the network-Sets is in same scope with SP

    Log    add netset2 to sp2      console=True
    ${resp}=  Edit Server Profile  ${Edit_sp_netsets1}
    Wait For Task2   ${resp}   timeout=600

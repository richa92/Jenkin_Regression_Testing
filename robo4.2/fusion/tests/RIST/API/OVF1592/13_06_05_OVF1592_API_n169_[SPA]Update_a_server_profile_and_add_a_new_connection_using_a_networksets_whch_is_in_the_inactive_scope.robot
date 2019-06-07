*** Settings ***
Documentation        Server Profiles Associated with network-Sets Update a server profile and add a new connection using an network-Sets, the network-Sets is in the inactive scope
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
[SPA] - Server Profiles Associated with network-Sets Update a server profile and add a new connection using an network-Sets, the network-Sets is in different scope with SP
    [Documentation]  OVF1592 API n169 [Server Profile Administrator] Server Profiles Associated with network-Sets Update a server profile and add a new connection using an network-Sets, the network-Sets is in the inactive scope

    Log     Edit server profiles sp2 with add netset4      console=True
    ${resp}=  Edit Server Profile  ${Edit_sp_netsets3}
    Wait For Task2   ${resp}   timeout=600   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
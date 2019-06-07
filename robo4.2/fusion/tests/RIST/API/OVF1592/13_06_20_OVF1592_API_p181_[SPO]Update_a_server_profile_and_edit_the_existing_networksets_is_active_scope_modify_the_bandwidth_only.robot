*** Settings ***
Documentation        Server Profiles Associated with network-Sets Update a server profile and edit the existing connection which related network-Sets is in the active scope, modify the bandwidth only
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["spo_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
[SPO] - Server Profiles Associated with network-Sets Update a server profile and edit the existing connection which related network-Sets is in the active scope, modify the bandwidth only    [Documentation]  OVF1592 API p181 [Server Profile Administrator] Server Profiles Associated with network-Sets Update a server profile and edit the existing connection which related network-Sets is in the active scope, modify the bandwidth only

    Log     Edit server profiles sp2 change port     console=True
    ${resp}=  Edit Server Profile  ${Edit_sp_netsets_port1}
    Wait For Task2   ${resp}   timeout=600

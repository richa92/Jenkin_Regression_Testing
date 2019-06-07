*** Settings ***
Documentation        Server Profiles Associated with Ethernet Update a server profile and edit the existing connection using ethernet, select a new ethernet which is in the inactive scope
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
[SPO] - Server Profiles Associated with Ethernet Update a server profile and edit the existing connection using ethernet, select a new ethernet which is in the inactive scope
    [Documentation]  OVF1592 API n171 [Server Profile Administrator] Server Profiles Associated with Ethernet Update a server profile and edit the existing connection using ethernet, select a new ethernet which is in the inactive scope

    Log     Can not change server profiles sp2 from eth2 to eth4      console=True
    ${resp}=  Edit Server Profile  ${Edit_sp_network3}
    Wait For Task2   ${resp}   timeout=600   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

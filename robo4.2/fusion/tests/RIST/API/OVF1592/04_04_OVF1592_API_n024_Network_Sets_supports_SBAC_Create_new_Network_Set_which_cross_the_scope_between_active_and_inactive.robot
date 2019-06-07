*** Settings ***
Documentation        Network Sets supports SBAC Create new Network Set which cross the scope between active and inactive
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

Test Setup      Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
Test Teardown   Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Network Sets supports SBAC Create new Network Set which cross the scope between active and inactive
    [Documentation]  OVF1592 API n024 Network Sets supports SBAC Create new Network Set which cross the scope between active and inactive
    Log     Creating Network net-set6 with Stage and test scopes   console=True
    ${resp}=      Add Networks Sets From Variable Async     ${create_network_set3}    status_code=403

    ${resps}=    Common URI lookup by name     network-setV\\d*:${new_NS_name2}
    should be equal  '${resps}'    '/rest/network_set_uri_${new_NS_name2}_not_found'


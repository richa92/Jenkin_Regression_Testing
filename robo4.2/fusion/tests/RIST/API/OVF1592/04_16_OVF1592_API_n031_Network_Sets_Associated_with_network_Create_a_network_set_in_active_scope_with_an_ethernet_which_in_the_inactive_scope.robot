*** Settings ***
Documentation        Network Sets Associated with network Create a network set in active scope with an ethernet which in the inactive scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Network Sets Associated with network Create a network set in active scope with an ethernet which in the inactive scope
  [Documentation]  OVF1592 API n031 Network Sets Associated with network Create a network set in active scope with an ethernet which in the inactive scope

  Log   can not add eth4 to ns6 which in inactive scope
  ${resp}=      Add Networks Sets from variable async   ${create_network_set6}  status_code=403

  ${resps}=    Common URI lookup by name     network-setV\\d*:${new_NS_name2}
  should be equal  '${resps}'    '/rest/network_set_uri_${new_NS_name2}_not_found'

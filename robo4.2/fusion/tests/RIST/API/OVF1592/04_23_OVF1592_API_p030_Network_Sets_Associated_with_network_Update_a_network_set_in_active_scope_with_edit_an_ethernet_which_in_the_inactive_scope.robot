*** Settings ***
Documentation        Network Sets Associated with network Update a network set in active scope with edit an ethernet which in the inactive scope
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
Network Sets Associated with network Update a network set in active scope with edit an ethernet which in the inactive scope
  [Documentation]  OVF1592 API p030 Network Sets Associated with network Update a network set in active scope with edit an ethernet which in the inactive scope
   Log  update ns1 add eth4 native
   ${resps}=   Update Network Set    ${update_network_set6}

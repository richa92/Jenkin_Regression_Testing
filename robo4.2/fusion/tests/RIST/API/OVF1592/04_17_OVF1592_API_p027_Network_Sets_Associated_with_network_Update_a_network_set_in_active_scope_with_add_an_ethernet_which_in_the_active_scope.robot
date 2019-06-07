*** Settings ***
Documentation        Network Sets Associated with network Update a network set in active scope with add an ethernet which in the active scope
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
Network Sets Associated with network Update a network set in active scope with add an ethernet which in the active scope
  [Documentation]  OVF1592 API p027 Network Sets Associated with network Update a network set in active scope with add an ethernet which in the active scope
  log    update Network Set net-set1    console=True
  ${resps}=   Update Network Set    ${update_network_set2}

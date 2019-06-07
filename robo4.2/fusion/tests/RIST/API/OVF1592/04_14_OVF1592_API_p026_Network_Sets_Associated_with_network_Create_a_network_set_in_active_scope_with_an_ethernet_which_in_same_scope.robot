*** Settings ***
Documentation        Network Sets Associated with network Create a network set in active scope with an ethernet which in same scope
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

Suite Setup             Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Network Sets Associated with network Create a network set in active scope with an ethernet which in same scope

  [Documentation]  OVF1592 API p026 Network Sets Associated with network Create a network set in active scope with an ethernet which in same scope
  Log     Create ns5 test with network eth2 which in active scope
  ${resps}=      Add Networks Sets from variable async   ${create_network_set4}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  network-setV\\d*:${new_NS_name}  ${TRUE}

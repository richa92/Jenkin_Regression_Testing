*** Settings ***
Documentation        Network Sets supports SBAC Create new Network Set which is in the active scope
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Network Sets supports SBAC Create new Network Set which is in the active scope
  [Documentation]  OVF1592 API p020 Network Sets supports SBAC Create new Network Set which is in the active scope

  log   Creating Network net-set5 with Test scope   console=True
  ${resps}=      Add Networks Sets from variable async   ${create_network_set}

  log     Check scopes information  console=True
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[0]}  network-setV\\d*:${new_NS_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  network-setV\\d*:${new_NS_name}  ${TRUE}

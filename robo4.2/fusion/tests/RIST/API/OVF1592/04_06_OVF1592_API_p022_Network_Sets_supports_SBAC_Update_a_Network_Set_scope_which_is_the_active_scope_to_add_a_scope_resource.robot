*** Settings ***
Documentation        Network Sets supports SBAC Update a Network Set scope which is the active scope to add a scope resource
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
Network Sets supports SBAC Update a Network Set scope which is the active scope to add a scope resource
  [Documentation]  OVF1592 API p022 Network Sets supports SBAC Update a Network Set scope which is the active scope to add a scope resource

  log      body data   console=True
  ${resp}=   Patch Resources Scopes  NS:${network_set_list[1]}   ${Patch_add_Scope3}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[3]}  network-setV\\d*:${network_set_list[1]}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  network-setV\\d*:${network_set_list[1]}  ${TRUE}

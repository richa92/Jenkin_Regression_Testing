*** Settings ***
Documentation        Network Sets supports SBAC Update a Network Set scope which is in the active scope to add a scope which is not the resource of this active scope
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
Network Sets supports SBAC Update a Network Set scope which is in the active scope to add a scope which is not the resource of this active scope
  [Documentation]  OVF1592 API n026 Network Sets supports SBAC Update a Network Set scope which is in the active scope to add a scope which is not the resource of this active scope

  ${resp}=   Patch Resources Scopes  NS:${network_set_list[2]}   ${Patch_add_Scope3}
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[3]}  network-setV\\d*:${network_set_list[2]}  ${False}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[0]}  network-setV\\d*:${network_set_list[2]}  ${TRUE}

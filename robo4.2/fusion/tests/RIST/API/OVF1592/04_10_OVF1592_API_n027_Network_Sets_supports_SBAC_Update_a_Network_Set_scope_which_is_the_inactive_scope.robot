*** Settings ***
Documentation        Network Sets supports SBAC Update a Network Set scope which is the inactive scope
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
Network Sets supports SBAC Update a Network Set scope which is the inactive scope
  [Documentation]  OVF1592 API n027 Network Sets supports SBAC Update a Network Set scope which is the inactive scope

  ${resp}=   Patch Resources Scopes  NS:${network_set_list[3]}   ${Patch_add_Scope5}
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[2]}  network-setV\\d*:${network_set_list[3]}  ${True}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[5]}  network-setV\\d*:${network_set_list[3]}  ${False}

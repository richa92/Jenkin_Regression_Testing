*** Settings ***
Documentation        FC supports SBAC Update an FC network scope which is the inactive scope
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
FC supports SBAC Update an FC network scope which is the inactive scope
  [Documentation]  OVF1592 API n013 FC supports SBAC Update an FC network scope which is the inactive scope

  Log  Add scopes3 to fc4    console=True
  ${resps}=   Patch Resources Scopes   FC:${fc_networks[3]['name']}   ${Patch_add_Scope5}
  Should Match Regexp         ${resps['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps['status_code']}'    '403'
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}   FC:${fc_networks[3]["name"]}  ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[5]}   FC:${fc_networks[3]["name"]}  ${False}

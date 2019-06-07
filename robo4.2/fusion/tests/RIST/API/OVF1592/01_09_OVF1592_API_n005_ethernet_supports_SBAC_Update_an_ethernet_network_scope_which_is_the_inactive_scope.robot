*** Settings ***
Documentation        Update an ethernet network scope which is the inactive scope
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
Update an ethernet network scope which is the inactive scope
  [Documentation]  OVF1592 API n005 ethernet supports SBAC Update an ethernet network scope which is the inactive scope

  Log  add scopes3 to eth4    console=True
  ${resp}=   Patch Resources Scopes  ETH:${Ethernet_Networks[3]['name']}   ${Patch_add_Scope5}
  Should Match Regexp      ${resp['message']}   ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resp['status_code']}'    '403'
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}   ETH:${Ethernet_Networks[3]["name"]}  ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[5]}   ETH:${Ethernet_Networks[3]["name"]}  ${FALSE}

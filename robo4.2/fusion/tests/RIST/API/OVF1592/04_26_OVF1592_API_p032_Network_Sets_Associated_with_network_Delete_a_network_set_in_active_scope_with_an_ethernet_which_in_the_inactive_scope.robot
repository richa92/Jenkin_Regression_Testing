*** Settings ***
Documentation        Delete a network set in active scope with an ethernet which in the inactive scope
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

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Delete a network set in active scope with an ethernet which in the inactive scope
  [Documentation]  OVF1592 API p032 Network Sets Associated with network Delete a network set in active scope with an ethernet which in the inactive scope
  Log    Delete active scope of ns1
  ${resps}=    Fusion Api Delete Network Set  name=${network_set_list[0]}
  Wait For Task2  ${resps}

  Log     check network set information
  ${netset_uri_result}=   Get Network Set Uri   ${network_set_list[0]}
  Should Be Equal  '${netset_uri_result}'   '/rest/network_set_uri_${network_set_list[0]}_not_found'
  Logout Appliance

  Login Appliance    ${APPLIANCE_IP}    ${credentials["admin_credentials"]}
  ${net_set1}=    Create List    ${network_sets[0]}
  Add Network Sets From Variable    ${net_set1}
  Logout Appliance
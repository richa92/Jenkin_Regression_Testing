*** Settings ***
Documentation        Network Sets supports SBAC Delete a Network Set which in the inactive scope
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
Network Sets supports SBAC Delete a Network Set which in the inactive scope
  [Documentation]  OVF1592 API n029 Network Sets supports SBAC Delete a Network Set which in the inactive scope

  Log    Delete active scope of ns4
  ${resps}=    Fusion Api Delete Network Set  name=${network_set_list[3]}
   Wait For Task2   ${resps}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True

  Log     check network set information
  ${netset_uri_result}=   Get Network Set Uri   ${network_set_list[3]}
  Should Not Be Equal  '${netset_uri_result}'   '/rest/network_set_uri_${network_set_list[3]}_not_found'
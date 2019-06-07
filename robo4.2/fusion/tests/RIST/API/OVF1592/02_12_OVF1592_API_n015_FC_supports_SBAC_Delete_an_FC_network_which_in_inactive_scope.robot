*** Settings ***
Documentation        FC supports SBAC Delete an FC network which in inactive scope
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
FC supports SBAC Delete an FC network which in inactive scope
  [Documentation]  OVF1592 API n015 FC supports SBAC Delete an FC network which in inactive scope

  Log   Get fc uri    console=True
  ${resps}=    Fusion Api Delete fc Network  name=${fc_networks[3]["name"]}

  Log  Check information    console=True
  Should Match Regexp         ${resps['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps['status_code']}'    '403'
  ${FC_Uri_Result}=    Get fc Uri  ${fc_networks[3]["name"]}
  Should Not Contain  '${FC_Uri_Result}'   '/rest/fc_network_uri_${fc_networks[3]["name"]}_not_found
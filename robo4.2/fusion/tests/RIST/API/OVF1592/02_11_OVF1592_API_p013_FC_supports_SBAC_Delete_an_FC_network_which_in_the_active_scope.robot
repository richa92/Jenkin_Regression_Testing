*** Settings ***
Documentation        FC supports SBAC Delete an FC network which in the active scope
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
FC supports SBAC Delete an FC network which in the active scope
  [Documentation]  OVF1592 API p013 FC supports SBAC Delete an FC network which in the active scope

  Log  Get fc uri    console=True
  ${resp}=    Delete Resource  FC:${new_fc_name}
  wait for task2  ${resp}

  Log    Check fc_network information    console=True
  ${fc_uri_result}=    Get FC URI   ${new_fc_name}
  should be equal  '${fc_uri_result}'   '/rest/fc_network_uri_${new_fc_name}_not_found'

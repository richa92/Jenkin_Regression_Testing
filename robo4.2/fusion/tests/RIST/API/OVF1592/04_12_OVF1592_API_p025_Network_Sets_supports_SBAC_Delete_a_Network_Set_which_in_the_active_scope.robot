*** Settings ***
Documentation        Network_Sets supports_SBAC Delete a Network Set which in the active scope
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
Network_Sets supports_SBAC Delete a Network Set which in the active scope
  [Documentation]  OVF1592 API p025 Network_Sets supports_SBAC Delete a Network Set which in the active scope

  Log    Delete active scope of ns3
  ${resps}=    Fusion Api Delete Network Set  name=${new_NS_name}
  Wait For Task2  ${resps}

  Log     check network set information
  ${netset_uri_result}=   Get Network Set Uri   ${new_NS_name}
  Should Be Equal  '${netset_uri_result}'   '/rest/network_set_uri_${new_NS_name}_not_found'
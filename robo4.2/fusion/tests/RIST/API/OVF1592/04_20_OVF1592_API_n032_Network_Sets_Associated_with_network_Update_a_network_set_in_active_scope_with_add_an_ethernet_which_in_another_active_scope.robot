*** Settings ***
Documentation        Network Sets Associated with network Update a network set in active scope with add an ethernet which in another active scope
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
Network Sets Associated with network Update a network set in active scope with add an ethernet which in another active scope
   [Documentation]  OVF1592 API n032 Network Sets Associated with network Update a network set in active scope with add an ethernet which in another active scope

   Log  can not update ns2 which was add eth3
  ${resp} =  Update Network Set     ${update_network_set9}
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

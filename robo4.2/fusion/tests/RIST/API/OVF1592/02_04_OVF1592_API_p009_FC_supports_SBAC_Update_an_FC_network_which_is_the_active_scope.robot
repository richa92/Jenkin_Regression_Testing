*** Settings ***
Documentation        FC supports SBAC Update an FC network which is the active scope
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
FC supports SBAC Update an FC network which is the active scope
  [Documentation]  OVF1592 API p009 FC supports SBAC Update an FC network which is the active scope
   Set Log Level  TRACE
   Log   Set "fc1" name to "fc5"    console=True
   ${resp}=   Update FC Network    ${fc_networks[0]["name"]}  ${update_fc_network}
   Wait For Task2    ${resp}

   Log   Restore Network reset name to "fc1"    console=True
   ${resps}=   Update FC Network   ${update_fc_network[0]["name"]}     ${update_fc_network2}
   Wait For Task2    ${resps}

*** Settings ***
Documentation        Enclosure Groups Associated with network_Create a EG which in active scope with an ethernet which in the other active scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups Associated with network_Create a EG which in active scope with an ethernet which in the other active scope
  [Documentation]  OVF1592 API n184 Enclosure Groups Associated with network_Create a EG which in active scope with an ethernet which in the other active scope

  Log   Can not Create new Enclosure Groups EG6 with network3 which inactive    console=True
  ${resp}=  Add Enclosure Group From Variable  ${create_EG_Network2}
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

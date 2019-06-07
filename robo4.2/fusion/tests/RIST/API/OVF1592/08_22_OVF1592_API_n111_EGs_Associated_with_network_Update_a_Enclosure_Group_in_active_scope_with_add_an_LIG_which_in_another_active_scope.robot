*** Settings ***
Documentation        Enclosure Groups Associated with network_Update a Enclosure Group in active scope with add an LIG which in another active scope
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
Enclosure Groups Associated with network_Update a Enclosure Group in active scope with add an LIG which in another active scope
  [Documentation]  OVF1592 API n111 Enclosure Groups Associated with network_Update a Enclosure Group in active scope with add an LIG which in another active scope

  Log   ADD lig3 to EG5     console=True
  ${resps}=  Edit Enclosure Group    ${Edit_EG8}
  Wait For Task2   ${resps}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

*** Settings ***
Documentation        Enclosure Groups supports SBAC_Update a EG which in the inactive scope
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
Enclosure Groups supports SBAC_Update a EG which in the inactive scope
  [Documentation]  OVF1592 API n107 Enclosure Groups supports SBAC_Update a EG which in the inactive scope

  Log   Edit Enclosure Groups EG4 which in inative scope   console=True
  ${resps}=  Edit Enclosure Group    ${Edit_EG2}
  Wait For Task2   ${resps}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True

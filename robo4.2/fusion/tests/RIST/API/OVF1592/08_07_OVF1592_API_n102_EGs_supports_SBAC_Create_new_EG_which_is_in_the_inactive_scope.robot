*** Settings ***
Documentation        Enclosure Groups supports SBAC_Create new EG which is in the inactive scope
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
Enclosure Groups supports SBAC_Create new EG which is in the inactive scope
  [Documentation]  OVF1592 API n102 Enclosure Groups supports SBAC_Create new EG which is in the inactive scope

  Log   Create new Enclosure Groups EG6 with inactive scope    console=True
  ${resp}=  Add Enclosure Group From Variable  ${create_EG2}
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${creation_not_authorized_error}    VERBOSE=True

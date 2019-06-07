*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC Update a LIG which in the inactive scope
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Logical Interconnect Groups supports SBAC Update a LIG which in the inactive scope
  [Documentation]  OVF1592 API n064 Logical Interconnect Groups supports SBAC Update a LIG which in the inactive scope

   Log   Can not Edit Logical interconnect group LIG4    console=True
   ${resp}=   Edit Lig    ${update_lig2}
   Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True

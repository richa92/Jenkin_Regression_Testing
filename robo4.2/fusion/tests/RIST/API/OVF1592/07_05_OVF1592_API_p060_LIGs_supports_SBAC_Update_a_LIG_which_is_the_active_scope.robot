*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC Update a LIG which is the active scope
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown         Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Logical Interconnect Groups supports SBAC Update a LIG which is the active scope
  [Documentation]  OVF1592 API p060 Logical Interconnect Groups supports SBAC Update a LIG which is the active scope

   Log   Edit Logical interconnect group LIG5    console=True
   ${resp}=   Edit Lig    ${update_lig1}
   Wait For Task2   ${resp}
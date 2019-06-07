*** Settings ***
Documentation        Interconnects supports SBAC Does not have the right on power on off reset if the inteconnect in inactive scope
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
Interconnects supports SBAC Does not have the right on power on off reset if the inteconnect in inactive scope
  [Documentation]  OVF1592 API n039 Interconnects supports SBAC Does not have the right on power on off reset if the inteconnect in inactive scope

  Log  Can not power on inter4
  ${resp}=   Patch Interconnect   ${interconect_name[1]}   op=replace   path=/powerState   value=Off
  Wait For Task2   ${resp}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
  ${resps}=   Patch Interconnect  ${interconect_name[1]}   op=replace   path=/deviceResetState   value=Reset
  Wait For Task2   ${resps}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True

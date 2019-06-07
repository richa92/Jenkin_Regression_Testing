*** Settings ***
Documentation        Interconnects supports SBAC Has the right on power on off reset if the inteconnect in active scope
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
Interconnects supports SBAC Has the right on power on off reset if the inteconnect in active scope
  [Documentation]  OVF1592 API p037 Interconnects supports SBAC Has the right on power on/power off/reset if the inteconnect in active scope
  Log  power on inter1
  ${resp}=   Patch Interconnect   ${interconect_name[0]}   op=replace   path=/powerState   value=Off
  ${respss}=   Patch Interconnect   ${interconect_name[0]}   op=replace   path=/powerState   value=On
#  sleep   30
#  ${resps}=   Patch Interconnect  ${interconect_name[0]}   op=replace   path=/deviceResetState   value=Reset

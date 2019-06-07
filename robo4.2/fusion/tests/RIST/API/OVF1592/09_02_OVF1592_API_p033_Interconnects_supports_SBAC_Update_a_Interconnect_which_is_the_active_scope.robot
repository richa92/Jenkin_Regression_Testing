*** Settings ***
Documentation        Interconnects supports SBAC Update a Interconnect which is the active scope
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
Interconnects supports SBAC Update a Interconnect which is the active scope
  [Documentation]  OVF1592 API p033 Interconnects supports SBAC Update a Interconnect which is the active scope
  Log  Update IC2 which is in active scope
  ${resp}=  Update Ic Port   ${interconects_list[1]}       ${DownLinkPort}   ${update_IC}
  Wait For Task2  ${resp}

*** Settings ***
Documentation        Enclosure Groups Associated with network_Update a EG which in active scope with an ethernet which in same scope
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
Enclosure Groups Associated with network_Update a EG which in active scope with an ethernet which in same scope
  [Documentation]  OVF1592 API p201 Enclosure Groups Associated with network_Update a EG which in active scope with an ethernet which in same scope

  Log   ADD eth1 to EG5     console=True
  ${resps}=  Edit Enclosure Group    ${Edit_network_EG1}
  Wait For Task2   ${resps}   timeout=60
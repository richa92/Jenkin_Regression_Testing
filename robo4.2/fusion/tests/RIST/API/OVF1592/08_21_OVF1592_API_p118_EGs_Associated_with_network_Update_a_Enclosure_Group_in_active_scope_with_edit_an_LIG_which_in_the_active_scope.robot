*** Settings ***
Documentation        Enclosure Groups Associated with network_Update a Enclosure Group in active scope with edit an LIG which in the active scope
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
Enclosure Groups Associated with network_Update a Enclosure Group in active scope with edit an LIG which in the active scope
  [Documentation]  OVF1592 API p118 Enclosure Groups Associated with network_Update a Enclosure Group in active scope with edit an LIG which in the active scope

  Log   change EG5 of lig2 to lig1   console=True
  ${resps}=  Edit Enclosure Group    ${Edit_EG6}
  Wait For Task2   ${resps}   timeout=60

*** Settings ***
Documentation        Enclosure Groups Associated with network_Create a EG which in active scope with an ethernet which in same scope
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

Suite Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["sa_credentials"]}
Suite Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups Associated with network_Create a EG which in active scope with an ethernet which in same scope
  [Documentation]  OVF1592 API p200 Enclosure Groups Associated with network_Create a EG which in active scope with an ethernet which in same scope

  Log   Create new Enclosure Groups EG5 with network1    console=True
  ${resp}=  Add Enclosure Group From Variable  ${create_EG_Network1}
  Wait For Task2   ${resp}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  EG:${new_EG_name}   ${True}

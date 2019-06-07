*** Settings ***
Documentation        Enclosure Groups Associated with network_Create a Enclosure Group in active scope with an LIG which in same scope
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
Enclosure Groups Associated with network_Create a Enclosure Group in active scope with an LIG which in same scope
  [Documentation]  OVF1592 API p116 Enclosure Groups Associated with network_Create a Enclosure Group in active scope with an LIG which in same scope

  Log   Create new Enclosure Groups EG5 with lig2    console=True
  ${resp}=   Add Enclosure Group from variable  ${create_EG4}
  Wait For Task2   ${resp}  timeout=60
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  EG:${new_EG_name}   ${True}

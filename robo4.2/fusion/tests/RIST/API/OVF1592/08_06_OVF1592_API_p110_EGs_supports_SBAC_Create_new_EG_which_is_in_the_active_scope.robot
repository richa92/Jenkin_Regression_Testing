*** Settings ***
Documentation        Enclosure Groups Support Scope Add EG resources to scopes via EG Interface
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
Suite Teardown        Remove Enclosure Group By Name  ${new_EG_name}
*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Enclosure Groups Support Scope Add EG resources to scopes via EG Interface
  [Documentation]  OVF1592 API p105 Enclosure Groups Support Scope Add EG resources to scopes via EG Interface

  Log   Create new Enclosure Groups EG5 with active scope    console=True
  ${resp}=  Add Enclosure Group From Variable  ${create_EG1}
  Wait For Task2   ${resp}  timeout=60
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  EG:${new_EG_name}   ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  EG:${new_EG_name}   ${True}

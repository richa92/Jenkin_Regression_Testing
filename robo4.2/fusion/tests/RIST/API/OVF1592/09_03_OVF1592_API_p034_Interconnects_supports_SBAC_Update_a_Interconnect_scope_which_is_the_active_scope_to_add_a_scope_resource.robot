*** Settings ***
Documentation        Interconnects supports SBAC Update a Interconnect scope which is the active scope to add a scope resource
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
Interconnects supports SBAC Update a Interconnect scope which is the active scope to add a scope resource
  [Documentation]  OVF1592 API p034 Interconnects supports SBAC Update a Interconnect scope which is the active scope to add a scope resource
  log      Update an inter2 add scope1 to scopes     console=True
  ${resp}=   Patch Resources Scopes  IC:${interconects_list[1]}   ${Patch_add_Scope3}
  Wait For Task2  ${resp}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[3]}  InterconnectV\\d*:${interconects_list[1]}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope    ${Scope_List[1]}  InterconnectV\\d*:${interconects_list[1]}  ${TRUE}

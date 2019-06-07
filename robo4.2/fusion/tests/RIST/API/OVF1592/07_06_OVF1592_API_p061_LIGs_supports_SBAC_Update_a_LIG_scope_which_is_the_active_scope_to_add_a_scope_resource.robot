*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC Update a LIG scope which is the active scope to add a scope resource
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
Logical Interconnect Groups supports SBAC Update a LIG scope which is the active scope to add a scope resource
  [Documentation]  OVF1592 API p061 Logical Interconnect Groups supports SBAC Update a LIG scope which is the active scope to add a scope resource

  Log   Add scope1 to LIG2    console=True
  ${resp}=   Patch Resources Scopes  LIG:${LIG[1]}   ${Patch_add_Scope3}
  Wait For Task2  ${resp}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}   LIG:${LIG[1]}  ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}   LIG:${LIG[1]}  ${True}

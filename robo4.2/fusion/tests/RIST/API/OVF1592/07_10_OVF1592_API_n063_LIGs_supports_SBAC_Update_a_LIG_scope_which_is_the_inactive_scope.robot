*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC Update a LIG scope which is the inactive scope
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
Logical Interconnect Groups supports SBAC Update a LIG scope which is the inactive scope
  [Documentation]  OVF1592 API n063 Logical Interconnect Groups supports SBAC Update a LIG scope which is the inactive scope

  Log   Can not edit LIG4 scopes    console=True
  ${resps}=   Patch Resources Scopes  LIG:${LIG[3]}   ${Patch_add_Scope5}
  Wait For Task2   ${resps}   timeout=60   PASS=Error  errorMessage=${NOT_AUTHORIZED_ERROR}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  LIG:${LIG[3]}  ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[5]}  LIG:${LIG[3]}  ${false}

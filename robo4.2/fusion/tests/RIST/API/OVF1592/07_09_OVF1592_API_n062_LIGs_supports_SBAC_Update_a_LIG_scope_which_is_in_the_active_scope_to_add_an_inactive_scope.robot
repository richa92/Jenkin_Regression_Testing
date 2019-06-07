*** Settings ***
Documentation        Logical Interconnect Groups supports SBAC Update a LIG scope which is the active scope, but the active scope have no scope resources
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
Logical Interconnect Groups supports SBAC Update a LIG scope which is the active scope, but the active scope have no scope resources
  [Documentation]  OVF1592 API n062 Logical Interconnect Groups supports SBAC Update a LIG scope which is the active scope, but the active scope have no scope resources
  Log   add scope1 to LIG3    console=True
  ${resps}=   Patch Resources Scopes  LIG:${LIG[2]}   ${Patch_add_Scope3}
  Wait For Task2   ${resps}   timeout=60   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  LIG:${LIG[2]}  ${True}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  LIG:${LIG[2]}  ${false}

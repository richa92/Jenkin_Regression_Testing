*** Settings ***
Documentation        Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope
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


*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope
  [Documentation]  Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope
  log    Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp} =    Patch Resources Scopes  LI:${LI1}    ${Patch_add_Scope5}
  Wait For Task2   ${resp}   timeout=240   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  LI:${LI1}   ${TRUE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[5]}  LI:${LI1}   ${FALSE}
  log    Successfully! Test Case : OVF1592_API_n051 Logical Interconnect supports SBAC_Update an Logical Interconnect scope which is in the active scope to add a scope which is not the resource of this active scope    console=true

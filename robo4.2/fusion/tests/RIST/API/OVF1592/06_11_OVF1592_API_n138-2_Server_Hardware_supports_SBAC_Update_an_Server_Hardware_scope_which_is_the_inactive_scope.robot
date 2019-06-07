*** Settings ***
Documentation        Server Hardware supports SBAC_Update an Server Hardware scope which is the inactive scope
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
Server Hardware supports SBAC_Update an Server Hardware scope which is the inactive scope
  [Documentation]  OVF1592_API_n138-2 Server Hardware supports SBAC_Update an Server Hardware scope which is the inactive scope
  log    Server Hardware supports SBAC_Update an Server Hardware scope which is the inactive scope    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp} =    Patch Resources Scopes  SH:${sh_name}   ${Patch_add_Scope0}
  Wait For Task2   ${resp}   timeout=200   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${sh_name}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SH:${sh_name}  ${FALSE}
  log    Successfully! Test Case : OVF1592_API_n138-2 Server Hardware supports SBAC_Update an Server Hardware scope which is the inactive scope    console=true


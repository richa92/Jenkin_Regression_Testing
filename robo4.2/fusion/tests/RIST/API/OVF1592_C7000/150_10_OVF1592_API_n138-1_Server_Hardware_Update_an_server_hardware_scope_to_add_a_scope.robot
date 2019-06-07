*** Settings ***
Documentation        Server Hardware supports SBAC_Update an server hardware scope which is in the active scope to add a scope which is not the resource of this active scope
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
Variables            ./Regression_Data.py
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt


*** Variables ***
${APPLIANCE_IP}      unknown
${DataFile}         ./Regression_Data.py

*** Test Cases ***
Server Hardware supports SBAC_Update an server hardware scope which is in the active scope to add a scope which is not the resource of this active scope
  [Documentation]  Server Hardware supports SBAC_Update an server hardware scope which is in the active scope to add a scope which is not the resource of this active scope
  log    Server Hardware supports SBAC_Update an server hardware scope which is in the active scope to add a scope which is not the resource of this active scope    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp} =    Patch Resources Scopes  SH:${new_dl_sh_name}   ${Patch_Encs_Negative}
  ${resps}=  Get Task Tree    uri=${resp["headers"]["X-Task-URI"]}
  Should Match Regexp  ${resps["resource"]["taskErrors"][0]['message']}  ${errorMessages['ASSOCIATION_FORBIDDEN_BY_SCOPE']}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${new_dl_sh_name}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[2]}  SH:${new_dl_sh_name}  ${FALSE}
  log    Successfully! Test Case : OVF1592_API_n138-1 Server Hardware supports SBAC_Update an server hardware scope which is in the active scope to add a scope which is not the resource of this active scope    console=true

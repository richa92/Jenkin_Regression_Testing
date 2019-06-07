*** Settings ***
Documentation        Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope
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
Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope
  [Documentation]    Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    SH:${sh_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Fusion Api Logout Appliance
  log    Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp} =    Patch Resources Scopes  SH:${sh_name}   ${Patch_Encs_Remove_Negative}
  ${resps}=  Get Task Tree    uri=${resp["headers"]["X-Task-URI"]}
  Should Match Regexp  ${resps["resource"]["taskErrors"][0]['message']}  ${errorMessages['ASSOCIATION_FORBIDDEN_BY_SCOPE']}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${sh_name}  ${TRUE}
  log    Successfully! Test Case : OVF1592_API_n138 Server Hardware support SBAC_Update an Server which is the active scope to delete an active scope    console=true

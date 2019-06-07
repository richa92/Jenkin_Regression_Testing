*** Settings ***
Documentation        Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource
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
Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource
  [Documentation]  OVF1592 API p095 Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    SH:${sh_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Fusion Api Logout Appliance
  log    Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp} =    Patch Resources Scopes  SH:${sh_name}   ${Patch_add_Scope3}
  Wait For Task2    ${resp}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${sh_name}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  SH:${sh_name}  ${TRUE}
  log    Successfully! Test Case : OVF1592 API p095 Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource    console=true

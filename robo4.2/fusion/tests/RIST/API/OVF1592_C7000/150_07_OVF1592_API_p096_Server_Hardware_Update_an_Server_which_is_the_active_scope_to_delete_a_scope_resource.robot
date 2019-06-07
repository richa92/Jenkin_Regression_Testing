*** Settings ***
Documentation        Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource
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


Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown
${DataFile}         ./Regression_Data.py

*** Test Cases ***
Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource
  [Documentation]  OVF1592 API p096 Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource
  log    Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource    console=true
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resp} =    Patch Resources Scopes  SH:${sh_name}   ${Patch_Encs_Remove}
  Wait For Task2    ${resp}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${sh_name}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  SH:${sh_name}  ${FALSE}
  log    Successfully! Test Case : OVF1592 API p096 Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource    console=true

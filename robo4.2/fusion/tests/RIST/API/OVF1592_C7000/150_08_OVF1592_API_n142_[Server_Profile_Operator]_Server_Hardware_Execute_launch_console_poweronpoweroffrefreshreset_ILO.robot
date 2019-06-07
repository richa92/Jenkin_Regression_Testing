*** Settings ***
Documentation        [Server Profile Operator] Server Hardware support SBAC_Execute the operations (launch console/ power on/power off/refresh/reset ILO) for server hardware which in the inactive scopes
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
[Server Profile Operator] Server Hardware support SBAC_Execute the operations (launch console/ power on/power off/refresh/reset ILO) for server hardware which in the inactive scopes
  [Documentation]  [Server Profile Operator] Server Hardware support SBAC_Execute the operations (launch console/ power on/power off/refresh/reset ILO) for server hardware which in the inactive scopes
  log    [Server Profile Operator] Server Hardware support SBAC_Execute the operations (launch console/ power on/power off/refresh/reset ILO) for server hardware which in the inactive scopes    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    SH:${new_dl_sh_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}    add_flag=${False}
  Fusion Api Logout Appliance
  Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
  ${resps}=  Patch Server Hardware  name=${new_dl_sh_name}    op=replace    path=/name    value=new_dl_sh_name
  Should Match Regexp        ${resps['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps['status_code']}'    '403'
  log    Successfully! Test Case : OVF1592_API_n142 [Server Profile Operator] Server Hardware support SBAC_Execute the operations (launch console/ power on/power off/refresh/reset ILO) for server hardware which in the inactive scopes    console=true

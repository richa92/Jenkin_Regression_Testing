*** Settings ***
Documentation        [Server Profile Operator] Server Hardware support SBAC_Try to remove a server hardware which in the active scope
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
[Server Profile Operator] Server Hardware support SBAC_Try to remove a server hardware which in the active scope
  [Documentation]  [Server Profile Operator] Server Hardware support SBAC_Try to remove a server hardware which in the active scope
  log    [Server Profile Operator] Server Hardware support SBAC_Try to remove a server hardware which in the active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    SH:${new_dl_sh_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Fusion Api Logout Appliance
  Active Permission Session  ${edit_spo_users_permission}    ${credentials['spo_credentials']}
  ${uri} =  Get Server Hardware URI  ${new_dl_sh_name}
  ${resp} =  Fusion Api Delete Server Hardware  uri=${uri}
  Should Match Regexp        ${resp['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resp['status_code']}'    '403'
  log    Successfully! Test Case : OVF1592_API_n141 [Server Profile Operator] Server Hardware support SBAC_Try to remove a server hardware which in the active scope   console=true

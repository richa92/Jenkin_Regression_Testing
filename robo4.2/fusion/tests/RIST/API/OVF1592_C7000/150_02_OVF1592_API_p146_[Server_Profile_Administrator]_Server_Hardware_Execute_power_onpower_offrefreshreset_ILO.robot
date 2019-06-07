*** Settings ***
Documentation        Server Hardware support SBAC_Add a new DL server into the active scope
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
Server Hardware support SBAC_Add a new DL server into the active scope
  [Documentation]  Server Hardware support SBAC_Add a new DL server into the active scope
  log    Server Hardware support SBAC_Add a new DL server into the active scope    console=true
  Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
  Reset Server    ${new_dl_sh_name}
  ${state} =    Get Server Power    ${new_dl_sh_name}
  Run Keyword If    '${state}'=='On'    Power Off Server    ${new_dl_sh_name}
  ...                ELSE IF    '${state}'=='Off'    Power On Server    ${new_dl_sh_name}
  ${state} =    Get Server Power    ${new_dl_sh_name}
  Run Keyword If    '${state}'=='On'    Power Off Server    ${new_dl_sh_name}
  ...                ELSE IF    '${state}'=='Off'    Power On Server    ${new_dl_sh_name}
  ${resp} =    Refresh Server Hardware    ${new_dl_sh_name}
  Wait For Task2    ${resp}    300    5
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  SH:${new_dl_sh_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  SH:${new_dl_sh_name}  ${TRUE}
  log    Successfully! Test Case : OVF1592_API_p146 Server Hardware support SBAC_Add a new DL server into the active scope    console=true

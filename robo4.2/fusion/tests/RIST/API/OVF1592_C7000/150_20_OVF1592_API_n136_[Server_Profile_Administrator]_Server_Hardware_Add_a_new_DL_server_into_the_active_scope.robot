*** Settings ***
Documentation        [Server Profile Administrator] Server Hardware support SBAC_Add a new DL server into the active scope
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
[Server Profile Administrator] Server Hardware support SBAC_Add a new DL server into the active scope
  [Documentation]  [Server Profile Administrator] Server Hardware support SBAC_Add a new DL server into the active scope
  log    [Server Profile Administrator] Server Hardware support SBAC_Add a new DL server into the active scope    console=true
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resps} =    Add Server Hardware from variable  ${rackservers_Negative2}     404    403
  ${uri} =  Get Server Hardware URI  ${new_dl_sh_name}
  Should Match Regexp  '${uri}'    '*not_found  msg=Add SH which is in the inactive is faild
  log    Successfully! Test Case : OVF1592_API_n136 [Server Profile Administrator] Server Hardware support SBAC_Add a new DL server into the active scope    console=true

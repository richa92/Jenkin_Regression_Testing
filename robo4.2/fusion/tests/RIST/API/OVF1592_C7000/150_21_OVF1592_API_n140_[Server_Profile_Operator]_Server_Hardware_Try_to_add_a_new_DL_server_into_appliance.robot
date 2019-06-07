*** Settings ***
Documentation        [Server Profile Operator] Server Hardware support SBAC_Try to add a new DL server into appliance
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
[Server Profile Operator] Server Hardware support SBAC_Try to add a new DL server into appliance
  [Documentation]  [Server Profile Operator] Server Hardware support SBAC_Try to add a new DL server into appliance
  log    [Server Profile Operator] Server Hardware support SBAC_Try to add a new DL server into appliance    console=true
  Active Permission Session  ${edit_spo_users_permission}    ${credentials['spo_credentials']}
  ${resps} =    Add Server Hardware from variable  ${rackservers_Negative2}     404    403
  ${uri} =  Get Server Hardware URI  ${new_dl_sh_name}
  Should Match Regexp  '${uri}'    '*not_found  msg=Add SH which is in the inactive is faild
  log    Successfully! Test Case : OVF1592_API_n140 [Server Profile Operator] Server Hardware support SBAC_Try to add a new DL server into appliance    console=true

*** Settings ***
Documentation        [Server Profile Operator] Server Hardware support SBAC_Has read access for all server hardware
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
[Server Profile Operator] Server Hardware support SBAC_Has read access for all server hardware
  [Documentation]  [Server Profile Operator] Server Hardware support SBAC_Has read access for all server hardware
  log    [Server Profile Operator] Server Hardware support SBAC_Has read access for all server hardware    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${sh_uri_list} =    Create List
  :FOR    ${sh_name}    IN    @{sh_name_list}
  \       ${sh_uri}=   Get Server Hardware URI    ${sh_name}
  \       Append To List    ${sh_uri_list}    ${sh_uri}
  Active Permission Session  ${edit_spo_users_permission}    ${credentials['spo_credentials']}
  ${resps}=   Fusion Api Get Server Hardware
  :FOR   ${sh_name_members}   IN   @{resps["members"]}
  \   Should Contain  '${sh_name_list}'  '${sh_name_members["name"]}'
  \   Continue For Loop
  :FOR   ${sh_uri_members}   IN   @{resps["members"]}
  \   Should Contain  '${sh_uri_list}'  '${sh_uri_members["uri"]}'
  \   Continue For Loop
  log    Successfully! Test Case : OVF1592_API_p150 [Server Profile Operator] Server Hardware support SBAC_Has read access for all server hardware    console=true

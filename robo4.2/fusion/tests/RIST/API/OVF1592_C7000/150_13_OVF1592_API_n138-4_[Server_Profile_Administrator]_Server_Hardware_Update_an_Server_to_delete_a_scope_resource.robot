*** Settings ***
Documentation        [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource
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
[Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource
  [Documentation]  [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource
  log    [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource    console=true
  Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
  ${resp} =    Patch Resources Scopes  SH:${sh_name}   ${Patch_Encs_Remove}
  Should Be Equal            '${resp['status_code']}'    '401'
  Should Match Regexp        ${resp['message']}    ${errorMessages['AUTHORIZATION']}
  log    Successfully! Test Case : OVF1592_API_n138-4 [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to delete a scope resource    console=true

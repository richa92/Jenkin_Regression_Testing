*** Settings ***
Documentation        [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource
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
[Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource
  [Documentation]  OVF1592_API_n138-3 [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource
  log    [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource    console=true
  Active Permission Session  ${edit_spa_users_permission}    ${credentials['spa_credentials']}
  ${resp} =    Patch Resources Scopes  SH:${sh_name}   ${Patch_add_Scope3}
  Should Be Equal            '${resp['status_code']}'    '401'
  Should Match Regexp        ${resp['message']}    ${errorMessages['AUTHORIZATION']}
  log    Successfully! Test Case : OVF1592_API_n138-3 [Server Profile Administrator] Server Hardware support SBAC_Update an Server which is the active scope to add a scope resource    console=true

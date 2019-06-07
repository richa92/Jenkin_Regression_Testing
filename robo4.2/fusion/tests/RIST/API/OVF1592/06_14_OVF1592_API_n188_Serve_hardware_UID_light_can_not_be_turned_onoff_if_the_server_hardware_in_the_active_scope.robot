*** Settings ***
Documentation        Serve hardware support SBAC_UID light can not be turned on/off if the server hardware in the active scope
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
Serve hardware support SBAC_UID light can not be turned on/off if the server hardware in the active scope
  [Documentation]  OVF1592_API_n188 Serve hardware support SBAC_UID light can not be turned on/off if the server hardware in the active scope
  log    Serve hardware support SBAC_UID light can not be turned on/off if the server hardware in the active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    SH:${sh_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}    add_flag=${False}
  Fusion Api Logout Appliance
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resp}=  Patch Server Hardware  ${sh_name}  op=replace  path=/uidState  value=On
  Should Match Regexp        ${resp['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resp['status_code']}'    '403'
  ${resp}=  Patch Server Hardware  ${sh_name}  op=replace  path=/uidState  value=Off
  Should Match Regexp        ${resp['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resp['status_code']}'    '403'
  log    Successfully! Test Case : OVF1592_API_n188 Serve hardware support SBAC_UID light can not be turned on/off if the server hardware in the active scope    console=true
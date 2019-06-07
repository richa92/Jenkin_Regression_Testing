*** Settings ***
Documentation        Enclosures support SBAC_UID light can not be turned on/off if the enclosure in the active scope
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
Enclosures support SBAC_UID light can not be turned on/off if the enclosure in the active scope
  [Documentation]  Enclosures support SBAC_UID light can not be turned on/off if the enclosure in the active scope

  log    Enclosures support SBAC_UID light can not be turned on/off if the enclosure in the active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    ENC:${new_enc_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}    add_flag=${False}
  Fusion Api Logout Appliance
  Active Permission Session  ${edit_sa_users_permission}    ${credentials['sa_credentials']}
  ${resps}=  Patch Enclosure  name=${new_enc_name}    op=replace    path=/uidState    value=On
  log to console   resps_is_${resps}
  Should Match Regexp        ${resps['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps['status_code']}'    '403'
  ${resps}=  Patch Enclosure  name=${new_enc_name}    op=replace    path=/uidState    value=Off
  log to console   resps_is_${resps}
  Should Match Regexp        ${resps['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps['status_code']}'    '403'
  log    Successfully! Test Case : OVF1592_API_n187 Enclosures support SBAC_UID light can not be turned on/off if the enclosure in the active scope    console=true
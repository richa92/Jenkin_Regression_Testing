*** Settings ***
Documentation        Enclosures support SBAC_UID light can be turned onoff if the enclosure in the active scope
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
Enclosures support SBAC_UID light can be turned onoff if the enclosure in the active scope
  [Documentation]  OVF1592 API p202 Enclosures support SBAC_UID light can be turned onoff if the enclosure in the active scope
  log    Enclosures support SBAC_UID light can be turned onoff if the enclosure in the active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    ENC:${new_enc_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resps}=  Patch Enclosure  name=${new_enc_name}    op=replace    path=/uidState    value=On
  Wait For Task2    ${resps}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:${new_enc_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
  ${resps}=  Patch Enclosure  name=${new_enc_name}    op=replace    path=/uidState    value=Off
  Wait For Task2    ${resps}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:${new_enc_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
  log    Successfully! Test Case : OVF1592 API p202 Enclosures support SBAC_UID light can be turned onoff if the enclosure in the active scope    console=true


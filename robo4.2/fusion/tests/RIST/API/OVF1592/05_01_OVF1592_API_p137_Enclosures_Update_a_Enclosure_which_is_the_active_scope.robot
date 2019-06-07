*** Settings ***
Documentation        Enclosures supports SBAC_Update a Enclosure which is the active scope
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
Enclosures supports SBAC_Update a Enclosure which is the active scope
  [Documentation]  OVF1592 API p137 Enclosures supports SBAC_Update a Enclosure which is the active scope
  ${resources_list} =    Create List    ENC:${new_enc_name}
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  log    Update a new Enclosure which is in the active scope    console=true
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resps}=  Patch Enclosure  name=${new_enc_name}    op=replace    path=/name    value=wpst333
  Wait For Task2    ${resps}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:wpst333  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:wpst333  ${TRUE}
  ${resps}=  Patch Enclosure  name=wpst333    op=replace    path=/name    value=${new_enc_name}
  Wait For Task2    ${resps}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:${new_enc_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
  log    Successfully! Test Case : OVF1592 API p137 Enclosures supports SBAC_Update a Enclosure which is the active scope    console=true

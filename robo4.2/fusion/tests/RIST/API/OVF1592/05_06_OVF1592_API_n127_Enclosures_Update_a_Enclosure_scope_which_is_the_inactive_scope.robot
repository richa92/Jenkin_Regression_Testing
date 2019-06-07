*** Settings ***
Documentation        Enclosures supports SBAC_Update a Enclosure scope which is the inactive scope
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
Enclosures supports SBAC_Update a Enclosure scope which is the inactive scope
  [Documentation]  Enclosures supports SBAC_Update a Enclosure scope which is the active scope to delete an active scope
  log    Update a new Enclosure which is in the active scope    console=true
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resp} =    Patch Resources Scopes  ENC:${new_enc_name}   ${Patch_add_Scope5}
  Wait For Task2   ${resp}   timeout=200   PASS=Error  errorMessage=${ASSOCIATION_FORBIDDEN_BY_SCOPE}    VERBOSE=True

  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[5]}  ENC:${new_enc_name}  ${FALSE}
  log    Successfully! Test Case : OVF1592 API n127 Enclosures supports SBAC_Update a Enclosure scope which is the inactive scope    console=true

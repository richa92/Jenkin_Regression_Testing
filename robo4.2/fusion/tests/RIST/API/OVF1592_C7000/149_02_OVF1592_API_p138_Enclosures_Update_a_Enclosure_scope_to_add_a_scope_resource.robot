*** Settings ***
Documentation        Enclosures supports SBAC_Update a Enclosure scope which is the active scope to add a scope resource
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
Enclosures supports SBAC_Update a Enclosure scope which is the active scope to add a scope resource
  [Documentation]  OVF1592 API p138 Enclosures supports SBAC_Update a Enclosure scope which is the active scope to add a scope resource
  log    Update a new Enclosure which is in the active scope    console=true
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resp} =    Patch Resources Scopes  ENC:${new_enc_name}   ${Patch_Encs}
  Wait For Task2    ${resp}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[3]}  ENC:${new_enc_name}  ${TRUE}
  ${resp} =    Patch Resources Scopes  ENC:${new_enc_name}   ${Patch_Encs_Remove}
  Wait For Task2    ${resp}
  log    Successfully! Test Case : OVF1592 API p138 Enclosures supports SBAC_Update a Enclosure scope which is the active scope to add a scope resource    console=true

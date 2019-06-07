*** Settings ***
Documentation        Enclosures supports SBAC Add a new Enclosure which is in the active scope
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
Enclosures supports SBAC_Add a new Enclosure which is in the active scope
  [Documentation]  Enclosures supports SBAC Add a new Enclosure which is in the active scope
  log    Add a new Enclosure which is in the active scope    console=true
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  Add Enclosures from variable  ${Add_Encs}    timeout=40min
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[0]}  ENC:${new_enc_name}  ${FALSE}
  Validate Resource Assigned/Unassigned To Scope   ${Scope_List[1]}  ENC:${new_enc_name}  ${TRUE}
  log    Successfully! Test Case : OVF1592 API p136 Enclosures supports SBAC Add a new Enclosure which is in the active scope    console=true

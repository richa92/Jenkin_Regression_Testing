*** Settings ***
Documentation        OVF1592_API_p141 Enclosures supports SBAC_Delete a Enclosure which in the active scope
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
Enclosures supports SBAC_Update a Enclosure scope which is the iactive scope
  [Documentation]  Enclosures supports SBAC_Delete a Enclosure which in the inactive scope

  log    Enclosures supports SBAC_Delete a Enclosure which in the inactive scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${resources_list} =    Create List    ENC:${new_enc_name}
  Update Scope With Resources    scope_name=${Scope_List[1]}    resources_list=${resources_list}
  Fusion Api Logout Appliance
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}

  Remove Enclosure    ${new_enc_name}    param=?force=True

  log    Successfully! Test Case : OVF1592_API_p141 Enclosures supports SBAC Delete a Enclosure which in the active scope    console=true

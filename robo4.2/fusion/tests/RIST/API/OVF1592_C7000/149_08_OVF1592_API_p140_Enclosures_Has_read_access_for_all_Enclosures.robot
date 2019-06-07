*** Settings ***
Documentation        Enclosures supports SBAC_Has read access for all Enclosures
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
Enclosures supports SBAC_Has read access for all Enclosures
  [Documentation]  Enclosures supports SBAC_Has read access for all Enclosures
  log    Update a new Enclosure which is in the active scope    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${enc_uri_list} =    Create List
  :FOR    ${enc_name}    IN    @{enc_name_list}
  \       ${enc_uri}=   Get Enclosure URI  ${enc_name}
  \       Append To List    ${enc_uri_list}    ${enc_uri}
  Active Permission Session  ${edit_users_permission}    ${credentials['sa_credentials']}
  ${resps}=   Fusion Api Get Enclosures
  :FOR   ${enc_name_members}   IN   @{resps["members"]}
  \   Should Contain  '${enc_name_list}'  '${enc_name_members["name"]}'
  \   Continue For Loop
  :FOR   ${enc_uri_members}   IN   @{resps["members"]}
  \   Should Contain  '${enc_uri_list}'  '${enc_uri_members["uri"]}'
  \   Continue For Loop
  log    Successfully! Test Case : OVF1592 API p140 Enclosures supports SBAC_Has read access for all Enclosures    console=true

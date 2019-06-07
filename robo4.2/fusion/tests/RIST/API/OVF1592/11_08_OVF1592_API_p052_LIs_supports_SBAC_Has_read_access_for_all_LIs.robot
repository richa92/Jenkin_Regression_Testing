*** Settings ***
Documentation        Logical Interconnect supports SBAC_Has read access for all Logical Interconnect
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
Logical Interconnect supports SBAC_Has read access for all Logical Interconnect
  [Documentation]  Logical Interconnect supports SBAC_Has read access for all Logical Interconnect
  log    Logical Interconnect supports SBAC_Has read access for all Logical Interconnect    console=true
  Fusion Api Login Appliance      ${APPLIANCE_IP}    ${credentials['admin_credentials']}
  ${li_uri_list} =    Create List
  :FOR    ${li_name}    IN    @{li_name_list}
  \       ${li_uri}=   Get LI URI  ${li_name}
  \       Append To List    ${li_uri_list}    ${li_uri}
  Active Permission Session  ${edit_ia_users_permission}    ${credentials['ia_credentials']}
  ${resps}=   Fusion Api Get LI
  :FOR   ${li_name_members}   IN   @{resps["members"]}
  \   Should Contain  '${li_name_list}'  '${li_name_members["name"]}'
  \   Continue For Loop
  :FOR   ${li_uri_members}   IN   @{resps["members"]}
  \   Should Contain  '${li_uri_list}'  '${li_uri_members["uri"]}'
  \   Continue For Loop
  log    Successfully! Test Case : OVF1592_API_p052 Logical Interconnect supports SBAC_Has read access for all Logical Interconnect    console=true

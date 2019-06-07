*** Settings ***
Documentation        Server Profiles supports SBAC Has read access for all Server Profiles
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["ia_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
Server Profiles supports SBAC Has read access for all Server Profiles
  [Documentation]  OVF1592 API p160 Server Profiles supports SBAC Has read access for all Server Profiles

   ${sp_uris}=   Get Server Profile URIS    ${sp_list}
   ${resps}=   Fusion Api Get Server Profiles
   should be equal  '${resps['count']}'   '4'
   :FOR   ${sp_name_members}   IN   @{resps["members"]}
   \   Should Contain  '${sp_list}'  '${sp_name_members["name"]}'
   :FOR   ${fcoe_uri_members}   IN   @{resps["members"]}
   \   Should Contain  '${sp_uris}'  '${sp_name_members["uri"]}'

*** Settings ***
Documentation        FC supports SBAC Has read access for all FC network
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

Test Setup           Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
Test Teardown        Logout Appliance

*** Variables ***
${APPLIANCE_IP}      unknown


*** Test Cases ***
FC supports SBAC Has read access for all FC network
  [Documentation]  OVF1592 API p012 FC supports SBAC Has read access for all FC network

   ${fc_uri}=   GET FC URIS  ${fc_list}
   ${resps}=   Fusion Api Get fc Networks

   :FOR   ${fc_name_members}   IN   @{resps["members"]}
    \   Should Contain  '${fc_list}'  '${fc_name_members["name"]}'
    \   Continue For Loop
   :FOR   ${fc_uri_members}   IN   @{resps["members"]}
    \   Should Contain  '${fc_uri}'  '${fc_uri_members["uri"]}'
    \   Continue For Loop

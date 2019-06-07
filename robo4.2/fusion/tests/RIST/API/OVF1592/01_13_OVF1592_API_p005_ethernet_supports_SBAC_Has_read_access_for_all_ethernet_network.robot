*** Settings ***
Documentation        Ethernet supports SBAC Has read access for all ethernet network
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
Ethernet supports SBAC Has read access for all ethernet network
  [Documentation]  OVF1592 API p005 ethernet supports SBAC Has read access for all ethernet network

   ${eth_uri}=   Get Ethernet URIs  ${eth_list}
   ${resps}=   Fusion Api Get Ethernet Networks

   :FOR   ${eth_name_members}   IN   @{resps["members"]}
    \   Should Contain  '${eth_list}'  '${eth_name_members["name"]}'
    \   Continue For Loop
   :FOR   ${eth_uri_members}   IN   @{resps["members"]}
    \   Should Contain  '${eth_uri}'  '${eth_uri_members["uri"]}'
    \   Continue For Loop
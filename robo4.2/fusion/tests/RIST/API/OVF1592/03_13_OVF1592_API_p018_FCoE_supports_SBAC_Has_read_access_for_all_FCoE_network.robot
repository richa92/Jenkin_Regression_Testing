*** Settings ***
Documentation        FCoE supports SBAC Has read access for all FCoE network
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
FCoE supports SBAC Has read access for all FCoE network
  [Documentation]  OVF1592 API p018 FCoE supports SBAC Has read access for all FCoE network

   ${fcoe_uri}=   GET FCOE URIS  ${fcoe_list}
   ${resps}=   Fusion Api Get fcoe Networks

    :FOR   ${fcoe_name_members}   IN   @{resps["members"]}
    \   Should Contain  '${fcoe_list}'  '${fcoe_name_members["name"]}'
    \   Continue For Loop
   :FOR   ${fcoe_uri_members}   IN   @{resps["members"]}
    \   Should Contain  '${fcoe_uri}'  '${fcoe_uri_members["uri"]}'
    \   Continue For Loop

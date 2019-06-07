*** Settings ***
Documentation        Network Sets supports SBAC Has read access for all Network Sets
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
Network Sets supports SBAC Has read access for all Network Sets
  [Documentation]  OVF1592 API p024 Network Sets supports SBAC Has read access for all Network Sets
   Log    read access for all Network Sets
   ${ns_uris}=   Get Network Set URIs    ${network_set_list}
   ${resps}=   Fusion Api Get Network Set
   Should Be Equal  '${resps['count']}'   '4'
    :FOR   ${ns_name_members}   IN   @{resps["members"]}
    \   Should Contain  '${network_set_list}'  '${ns_name_members["name"]}'
   :FOR   ${ns_uri_members}   IN   @{resps["members"]}
    \   Should Contain  '${ns_uris}'  '${ns_name_members["uri"]}'

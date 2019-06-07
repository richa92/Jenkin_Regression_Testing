*** Settings ***
Documentation        FCoE supports SBAC Delete an FCoE network which in the inactive scope
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
FCoE supports SBAC Delete an FCoE network which in the inactive scope
  [Documentation]  OVF1592 API n022 FCoE supports SBAC Delete an FCoE network which in the inactive scope

  Log   Get fcoe uri    console=True
  ${resps}=    Fusion Api Delete fcoe Network  name=${fcoe_networks[3]["name"]}

  Log  Check information    console=True
  Should Match Regexp         ${resps['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps['status_code']}'    '403'
  ${FCoe_Uri_Result}=    Get Fcoe Uri   ${fcoe_networks[3]["name"]}
  Should Not Contain  '${FCoe_Uri_Result}'   '/rest/fc_network_uri_${FCoe_Uri_Result}_not_found
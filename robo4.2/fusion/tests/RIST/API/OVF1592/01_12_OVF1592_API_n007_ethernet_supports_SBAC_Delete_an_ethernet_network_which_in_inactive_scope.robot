*** Settings ***
Documentation        Delete an ethernet network which in inactive scope
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
Delete an ethernet network which in inactive scope
  [Documentation]  OVF1592 API n007 ethernet supports SBAC Delete an ethernet network which in inactive scope

  Log  delete ethernet network    console=True
  ${resps}=    Fusion Api Delete Ethernet Network  ${Ethernet_Networks[3]["name"]}
  Should Match Regexp         ${resps['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps['status_code']}'    '403'

  ${Ethernet_Uri_Result}=    Get Ethernet Uri  ${Ethernet_Networks[3]["name"]}
  Should Not Contain  '${Ethernet_Uri_Result}'   '/rest/network_uri_${Ethernet_Networks[3]["name"]}_not_found'

*** Settings ***
Documentation        Ethernet supports SBAC Delete an ethernet network which in the active scope
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
Ethernet supports SBAC Delete an ethernet network which in the active scope
  [Documentation]  OVF1592 API p006 ethernet supports SBAC Delete an ethernet network which in the active scope

  Log  delete ethernet network    console=True
  ${resp}=    Delete Resource    ETH:${new_ethernet_name}
#  ${resp}=    Fusion Api Delete Ethernet Network  ${Ethernet_Networks[2]["name"]}
  Wait For Task2  ${resp}
  ${eth_uri_result}=    Get Ethernet Uri  ${new_ethernet_name}
  Should Contain  '${eth_uri_result}'   '/rest/network_uri_${new_ethernet_name}_not_found'

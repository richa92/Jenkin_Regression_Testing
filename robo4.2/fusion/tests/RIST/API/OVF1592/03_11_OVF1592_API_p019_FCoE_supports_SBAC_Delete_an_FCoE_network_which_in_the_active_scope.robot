*** Settings ***
Documentation        FCoE supports SBAC Delete an FCoE network which in the active scope
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
FCoE supports SBAC Delete an FCoE network which in the active scope
  [Documentation]  OVF1592 API p019 FCoE supports SBAC Delete an FCoE network which in the active scope

  Log  Get fcoe uri    console=True
  ${resps}=    Delete Resource  FCOE:${new_fcoe_name}
  Wait For Task2  ${resps}

  Log   Check fc_network information    console=True
  ${fcoe_uri_result}=    Get Fcoe Uri  ${new_fcoe_name}
  Should Be Equal  '${fcoe_uri_result}'   '/rest/network_uri_${new_fcoe_name}_not_found'

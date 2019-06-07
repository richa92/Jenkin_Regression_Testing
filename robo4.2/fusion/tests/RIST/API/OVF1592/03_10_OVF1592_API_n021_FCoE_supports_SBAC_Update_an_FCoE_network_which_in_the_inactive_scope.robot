*** Settings ***
Documentation        FCoE supports SBAC Update an FCoE network which in the inactive scope
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
FCoE supports SBAC Update an FCoE network which in the inactive scope
  [Documentation]  OVF1592 API n021 FCoE supports SBAC Update an FCoE network which in the inactive scope

   Log   Set "fcoe4" name to "fc5"    console=True
   ${resp}=   Update Fcoe Network    ${fcoe_networks[3]["name"]}  ${update_fcoe_network3}
   Should Match Regexp        ${resp['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
   Should Be Equal            '${resp['status_code']}'    '403'
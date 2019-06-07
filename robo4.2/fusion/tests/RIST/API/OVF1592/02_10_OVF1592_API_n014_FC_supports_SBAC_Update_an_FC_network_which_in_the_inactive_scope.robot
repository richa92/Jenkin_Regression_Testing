*** Settings ***
Documentation        FC supports SBAC Update an FC network which in the inactive scope
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
FC supports SBAC Update an FC network which in the inactive scope
  [Documentation]  OVF1592 API n014 FC supports SBAC Update an FC network which in the inactive scope

   Log   Set "fc4" name to "fc5"    console=True
   ${resp}=   Update FC Network    ${fc_networks[3]["name"]}  ${update_fc_network3}
   Should Match Regexp        ${resp['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
   Should Be Equal            '${resp['status_code']}'    '403'
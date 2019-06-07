*** Settings ***
Documentation        Update an ethernet network which in the inactive scope
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
Update an ethernet network which in the inactive scope
  [Documentation]  OVF1592 API n006 ethernet supports SBAC Update an ethernet network which in the inactive scope

   Log   set eth4 name to "eth5"    console=True
   ${resps}=  Edit Network     ${Update_Ethernet3}
   Should Match Regexp        ${resps[0]['rest_resp']['message']}    ${errorMessages['NOT_AUTHORIZED_ERROR']}
   Should Be Equal            '${resps[0]['rest_resp']['status_code']}'    '403'

*** Settings ***
Documentation        Ethernet supports SBAC Create new ethernet network whcih is in the inactive scope
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
Ethernet supports SBAC Create new ethernet network whcih is in the multiple inactive scope
  [Documentation]  OVF1592 API n002 ethernet supports SBAC Create new ethernet network which cross the scope between active and inactive

  Log  Creating Network    console=True
  ${resps}=  Add Ethernet Networks from variable      ${Create_Ethernet3}
  Should Match Regexp         ${resps[0]['message']}    ${errorMessages['CREATION_NOT_AUTHORIZED_ERROR']}
  Should Be Equal            '${resps[0]['status_code']}'    '403'

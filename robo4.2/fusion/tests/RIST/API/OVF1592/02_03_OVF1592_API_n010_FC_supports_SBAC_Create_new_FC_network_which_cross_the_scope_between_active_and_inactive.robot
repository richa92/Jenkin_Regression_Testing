*** Settings ***
Documentation        FC supports SBAC Create new FC network which cross the scope between active and inactive
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

Test Setup      Login Appliance  ${APPLIANCE_IP}    ${credentials["na_credentials"]}
Test Teardown   Logout Appliance
*** Variables ***
${APPLIANCE_IP}      unknown

*** Test Cases ***
FC supports SBAC Create new FC network which cross the scope between active and inactive
    [Documentation]  OVF1592 API n010 FC supports SBAC Create new FC network which cross the scope between active and inactive

    Log    Creating Networks    console=True
    ${resps}=     Add FC Networks from variable    ${create_fc_network3}  403
    Should Match Regexp         ${resps[0]['message']}    ${errorMessages['CREATION_NOT_AUTHORIZED_ERROR']}
    Should Be Equal            '${resps[0]['status_code']}'    '403'
    ${resp}=    Get FC URI     ${create_fc_network3[0]["name"]}
    Should Be Equal  '${resp}'    '/rest/fc_network_uri_${create_fc_network3[0]["name"]}_not_found'  msg=Create new FC which is cross the scope between active and inactive is faild

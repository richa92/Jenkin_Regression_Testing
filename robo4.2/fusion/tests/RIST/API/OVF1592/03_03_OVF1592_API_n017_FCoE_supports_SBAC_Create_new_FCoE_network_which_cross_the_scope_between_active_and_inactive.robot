*** Settings ***
Documentation        FCoE supports SBAC Create new FCoE network which cross the scope between active and inactive
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
FCoE supports SBAC Create new FCoE network which cross the scope between active and inactive
    [Documentation]  OVF1592 API n017 FCoE supports SBAC Create new FCoE network which cross the scope between active and inactive

    Log    Creating New Networks fcoe5    console=True
    ${resps}=      Add FCoE Networks from variable     ${create_fcoe_network3}
    Should Match Regexp         ${resps[0]['message']}    ${errorMessages['CREATION_NOT_AUTHORIZED_ERROR']}
    Should Be Equal            '${resps[0]['status_code']}'    '403'
    ${resp}=     Get FCoE URI     ${create_fcoe_network3[0]["name"]}
    Should Contain  '${resp}'    '/rest/network_uri_${create_fcoe_network3[0]["name"]}_not_found'  msg=Create new FCOE which is cross the scope between active and inactive is faild

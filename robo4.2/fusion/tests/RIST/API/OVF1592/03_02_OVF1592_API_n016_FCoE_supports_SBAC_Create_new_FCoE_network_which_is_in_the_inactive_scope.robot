*** Settings ***
Documentation        FCoE supports SBAC Create new FCoE network which is in the inactive scope
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
FCoE supports SBAC Create new FCoE network which is in the inactive scope
    [Documentation]  OVF1592 API n016 FCoE supports SBAC Create new FCoE network which is in the inactive scope
    Log    Creating New Networks fcoe5    console=True
    ${resps}=    Add FCoE Networks from variable     ${create_fcoe_network2}

    Log  Check status information    console=True
    Should Match Regexp         ${resps[0]['message']}    ${errorMessages['CREATION_NOT_AUTHORIZED_ERROR']}
    Should Be Equal            '${resps[0]['status_code']}'    '403'
    ${resp}=  Get FCoE URI      ${create_fcoe_network2[0]["name"]}
    Should Contain  '${resp}'    '/rest/network_uri_${create_fcoe_network2[0]["name"]}_not_found'  msg=Create new fcoe which is in the inactive is faild

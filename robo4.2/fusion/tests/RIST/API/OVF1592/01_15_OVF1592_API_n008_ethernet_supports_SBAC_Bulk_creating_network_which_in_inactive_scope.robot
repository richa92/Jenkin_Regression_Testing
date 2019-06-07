*** Settings ***
Documentation        Ethernet supports SBAC Bulk creating network which in inactive scope
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
Ethernet supports SBAC Bulk creating network which in inactive scope
    [Documentation]  OVF1592 API n008 ethernet supports SBAC Bulk creating network which in inactive scope

     Log  body data    console=True
     ${scopeUris}=    Run Keyword for List  ${bulk_create_ethernet2[0]["initialScopeUris"]}   Common URI lookup by name
     Set To Dictionary    ${bulk_create_ethernet2[0]}  initialScopeUris  ${scopeUris}
     ${resps}=  Fusion Api Create Ethernet Bulk Networks  ${bulk_create_ethernet2[0]}
     Should Match Regexp         ${resps['message']}    ${errorMessages['CREATION_NOT_AUTHORIZED_ERROR']}
     Should Be Equal            '${resps['status_code']}'    '403'

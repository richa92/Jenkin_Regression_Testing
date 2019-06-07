*** Settings ***
Documentation        OVF2422 query the index service to filter device certificates by mutiple items

Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ${DATA_FILE}
Test Setup           Fusion API Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
Test Teardown        Clear Testing Environment    ${RevocationCerts}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
As an Administrator want to query the index service to filter device certificate by by mutiple items
    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP14}
    ${resp} =  Validate Filtered Certs As Expected    ${resp['members']}    ${expectedCountP14}    ${queryCertsP14}
    Should Be True    ${resp}    msg=Fialed to filter out the target certs by by mutiple items

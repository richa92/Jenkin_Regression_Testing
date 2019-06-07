*** Settings ***
Documentation        OVF2422 query the index service to filter device certificates by cert state - Untrusted

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


*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
As an Administrator want to query the index service to filter device certificate by cert state - Untrusted
    ${resp} =  Delete Multiple CA Certificates    ${RevokedRoot}
    Wait for task2    ${resp}    50    5
    Fusion Api Get Certificate Status
    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP09}
    ${resp} =  Validate Filtered Certs As Expected    ${resp['members']}    ${expectedCountP09}    ${queryCertsP09}
    Should Be True    ${resp}    msg=Fialed to filter out the target certs by cert state untrusted

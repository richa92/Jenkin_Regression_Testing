*** Settings ***
Documentation        OVF2422 query the index service to filter certificates by cert state CRL NOT FOUND

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
As an Administrator want to query the index service to filter certs by cert type state CRL NOT FOUND
    Fusion Api Get Certificate Status
    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP05}
    ${resp} =  Validate Filtered Certs as Expected    ${resp['members']}    ${expectedCountP05}    ${queryCertsP05}
    Should Be True    ${resp}    msg=Failed to filter out the target certs by cert state CRL NOT FOUND

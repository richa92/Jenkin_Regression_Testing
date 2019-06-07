*** Settings ***
Documentation        OVF2422 query the index service to filter certificates by cert aliasname with fuzzy matching

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
As an Administrator want to query the index service to filter certificates by cert aliasname with fuzzy matching
    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP02}
    ${resp} =  Validate Filtered Certs as Expected    ${resp['members']}    ${expectedCountP02}    ${queryCertsP02}
    Should Be True    ${resp}    msg=Failed to filter out the target certs by aliasname with fuzzy matching

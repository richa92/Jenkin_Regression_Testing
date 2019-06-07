*** Settings ***
Documentation        OVF2422 query the index service to filter certificates by aliasname

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
As an Administrator want to query the index service to filter device certificate by aliasname
    ${resp} =  Import Multiple External CA Certificates      ${certs}
    Should Be True    ${resp}    msg=Failed to import multiple into OneView Trust Store

    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP01}
    ${resp} =  Validate Filtered Certs as Expected    ${resp['members']}    ${expectedCountP01}    ${queryCertsP01}
    Should Be True    ${resp}    msg=Failed to filter out the target certs by aliasname

*** Settings ***
Documentation        OVF2422 query the index service to filter certificates by cert state Expired

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
${item}    certStatus
${target_value}    EXPIRED

*** Test Cases ***
As an Administrator want to query the index service to filter certs by cert state Expired
    Fusion Api Get Certificate Status
    ${expectedCount} =  Get CA Certs Count By Specified Attribute    ${item}    ${target_value}
    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP06}
    ${resp} =  Validate Filtered Certs as Expected    ${resp['members']}    ${expectedCount}    ${queryCertsP06}
    Should Be True    ${resp}    msg=Failed to filter out the target certs by cert state Expired

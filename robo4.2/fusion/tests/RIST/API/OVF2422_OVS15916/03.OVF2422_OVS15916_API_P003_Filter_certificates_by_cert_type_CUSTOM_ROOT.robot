*** Settings ***
Documentation        OVF2422 query the index service to filter certificates by cert type CUSTOM ROOT

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
${item}    certType
${target_value}    CUSTOM_ROOT

*** Test Cases ***
As an Administrator want to query the index service to filter certs by cert type CUSTOM ROOT
    ${expectedCount} =  Get CA Certs Count By Specified Attribute    ${item}    ${target_value}
    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP03}
    ${resp} =  Validate Filtered Certs as Expected    ${resp['members']}    ${expectedCount}    ${queryCertsP03}
    Should Be True    ${resp}    msg=Failed to filter out the target certs by cert type CUSTOM ROOT

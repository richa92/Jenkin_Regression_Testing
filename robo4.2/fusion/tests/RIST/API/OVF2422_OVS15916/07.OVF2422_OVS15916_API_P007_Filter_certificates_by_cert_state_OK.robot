*** Settings ***
Documentation        OVF2422 query the index service to filter device certificates by cert state - OK

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
${aliasname}    Revocation_root_CA_filter_test

*** Test Cases ***
As an Administrator want to query the index service to filter device certificate by cert state - OK
    ${resp} =  Import Multiple External CA Certificates      ${RevocationCerts}
    Wait For Task2    ${resp}    50    5

    Log    upload CRL for the CA certificates    console=Yes
    ${localfile} =  Join Path    ${CURDIR}    \    ${filename}
    OperatingSystem.File Should Exist    ${localfile}
    ${resp} =  Fusion Api Upload CRL By Aliasname    ${aliasname}    ${localfile}
    Wait For Task2    ${resp}    50    5    None Expected    Completed
    Fusion Api Get Certificate Status
    ${resp} =  Filter Certificates by Multiple Parameters    ${queryCertsP07}
    ${resp} =  Validate Filtered Certs As Expected    ${resp['members']}    ${expectedCountP07}    ${queryCertsP07}
    Should Be True    ${resp}    msg=Fialed to filter out the target certs by cert state OK

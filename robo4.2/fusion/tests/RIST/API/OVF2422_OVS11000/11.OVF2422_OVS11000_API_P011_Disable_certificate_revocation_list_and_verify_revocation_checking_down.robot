*** Settings ***
Documentation        OVF2422 - Ensure certificate revocation list disabled and validate certificate revocation checking down

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
${aliasname}    shqa-WIN-D1VNB3UQSP2-CA


*** Test Cases ***
As an Administrator want to validate certificate revocation checking down after disable certificate revocation list
    Log    checking certificate validation configuration before updating    console=Yes
    Validate Certificate Validation Config As Expected    ${ConfigurationP10}
    Log    Import expired certificate to validate certificate basic checking take effect    console=Yes
    ${resp} =  Fusion Api Import External CA Certificates    ${RootCA[0]}
    Wait For Task2    ${resp}    70    5    None Expected    Completed

    Log    upload CRL which contents subca revoked info    console=Yes
    ${localfile} =  Join Path    ${CURDIR}    \    ${filename}
    OperatingSystem.File Should Exist    ${localfile}
    ${resp} =  Fusion Api Upload CRL By Aliasname    ${aliasname}    ${localfile}
    Wait For Task2    ${resp}    120    5    None Expected    Completed
    Log    import the revoked subCA   console=Yes
    ${resp} =  Fusion Api Import External CA Certificates    ${SubCA[0]}
    Wait For Task2    ${resp}    120    5    None Expected    Completed


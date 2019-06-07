*** Settings ***
Documentation        OVF2422 - Ensure certificate validation enabled and validate basic checking take effect

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
As an Administrator want to validate certificate basic checking take effect after enable certificate validation
    Log    checking certificate validation configuration before updating    console=Yes
    Validate Certificate Validation Config As Expected    ${DefaultConfig}
    Log    Import expired certificate to validate certificate basic checking take effect    console=Yes
    ${resp} =  Fusion Api Import External CA Certificates      ${expiredCert[0]}
    Wait For Task2       ${resp}     50    5   PASS=Error    errorMessage=Expired_Cert

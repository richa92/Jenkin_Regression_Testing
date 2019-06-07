*** Settings ***
Documentation        OVF2422 diaable certificate validation flag and validate trust checking down

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
Test Teardown        Clear Testing Environment    ${IntermediateCert}

*** Variables ***
${APPLIANCE_IP}       ${None}


*** Test Cases ***
As an Administrator want to validate certificate trust checking doesn't work with certificate validation disabled
    Log    Ensure certificate validation flag false before validation    console=Yes
    Validate Certificate Validation Config As Expected    ${configurationP02}
    Log    Import an intermediate certificate
    ${resp} =  Fusion Api Import External CA Certificates  ${IntermediateCert[0]}
    Wait For Task2       ${resp}    50    5   PASS=Error    errorMessage=Valid_Certificate_Chain

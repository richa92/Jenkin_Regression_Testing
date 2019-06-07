*** Settings ***
Documentation        OVF2422 disable certificate revocation list and validate the flag off

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
As an Administrator want to validate certificate revocation list flag is false after disabling CRL
    Log    checking certificate validation configuration before updating    console=Yes
    Validate Certificate Validation Config As Expected    ${DefaultConfig}
    Log    Update certificate validation configuration    console=Yes
    ${resp} =  Update Certificate Validation Configuration      ${ConfigurationP10}
    Should be true    ${resp}    msg=Failed to update certificate validation configuration
    Fusion API Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Log    valiadte certificate validation configuration has been updated as expected    console=Yes
    Validate Certificate Validation Config As Expected    ${ConfigurationP10}

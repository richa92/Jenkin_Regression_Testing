*** Settings ***
Documentation        OVF2422 enable revocation list and validate the flag is true

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
As an Administrator want to enable certificate revocation list and validate the flag is true
    Log    checking certificate validation configuration before updating    console=Yes
    Validate Certificate Validation Config As Expected    ${ConfigurationP10}
    Log    Update certificate validation configuration    console=Yes
    ${resp} =  Update Certificate Validation Configuration      ${DefaultConfig}
    Should Be True    ${resp}    msg=Failed to update certificate validation configuration
    Fusion API Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Log    valiadte certificate validation configuration has been updated as expected    console=Yes
    Validate Certificate Validation Config As Expected    ${DefaultConfig}

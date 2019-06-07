*** Settings ***
Documentation        OVF2422 enable certificate validation and validate the flag value true

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
As an Administrator want to enable certificate validation and validate the flag value is true
    Log    checking certificate validation configuration before updating    console=Yes
    Validate Certificate Validation Config As Expected    ${configurationP02}
    Log    Update certificate validation configuration    console=Yes
    ${resp} =  Update Certificate Validation Configuration      ${configurationP06}
    Should Be True    ${resp}    msg=Failed to enable certificate validation
    Fusion API Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Log    valiadte certificate validation configuration has been updated as expected    console=Yes
    Validate Certificate Validation Config As Expected    ${configurationP06}
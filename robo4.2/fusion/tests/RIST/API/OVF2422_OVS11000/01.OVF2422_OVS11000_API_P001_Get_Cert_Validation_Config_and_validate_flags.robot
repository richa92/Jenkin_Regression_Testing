*** Settings ***
Documentation        OVF2422 get certificate validation configuration and validate the flags' value by default

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
As an Administrator want to get certificate validation configuration and validate the flags value by default
    Log    \nchecking certificate validation configuration before updating    console=Yes
    Validate Certificate Validation Config As Expected    ${DefaultConfig}

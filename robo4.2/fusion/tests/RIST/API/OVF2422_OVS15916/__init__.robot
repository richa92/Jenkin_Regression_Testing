*** Settings ***
Library        FusionLibrary
Library        RoboGalaxyLibrary
Library        OperatingSystem
Library        Process
Library        SSHLibrary
Library        String
Library        Dialogs
Library        BuiltIn
Library        json
Library        Collections
Resource       ./../../../../Resources/api/fusion_api_resource.txt
Resource       ./keywords.txt
Variables      ${DATA_FILE}

Suite Setup     Precondition Setup
Suite Teardown  Clear Testing Environment    ${certs}

*** Variables ***
${APPLIANCE_IP}        ${None}


*** Keywords ***
Precondition Setup
    [Documentation]    Precondition Setup
    Set Log Level    TRACE
    Fusion API Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${resp} =  Update Certificate Validation Configuration    ${enableAlertForCRL}
    Should Be True    ${resp}    msg=Failed to update certificate validation configuration
    Fusion Api Logout Appliance
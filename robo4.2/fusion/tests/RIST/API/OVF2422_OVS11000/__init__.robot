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

Suite Setup  Precondition Setup
Suite Teardown  Check the latest cert status

*** Variables ***
${APPLIANCE_IP}        ${None}    #leave it as ${None} if you want this test to create a new one


*** Keywords ***
Precondition Setup
    [Documentation]    Precondition Setup
    Set Log Level    TRACE

Check the latest cert status
    [Documentation]    Check the latest cert status
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    ${resp} =  Run Keyword And Return Status    Validate Certificate Validation Config As Expected    ${DefaultConfig}
    Run Keyword If    ${resp}!=${True}    Update Certificate Validation Configuration    ${DefaultConfig}
    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Wait Until Keyword Succeeds    2min    5    Fusion Api Get Certificate Status
    Fusion Api Logout Appliance

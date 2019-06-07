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
Suite Teardown  Check the Latest Cert Status And Clean EVN

*** Variables ***
${APPLIANCE_IP}        ${None}    #leave it as ${None} if you want this test to create a new one


*** Keywords ***
Precondition Setup
    [Documentation]    Precondition Setup
    Set Log Level    TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    ${retrieve_appliance_cert} =  Fusion Api Get Appliance Certificate
    Log    \nGenerate certificate signing request    console=Yes
    ${generate_CSR} =  Create appliance signing request    ${appliance_cert_csr_body}
    log    ${generate_CSR[0]}
    ${generate_appliance_cert} =  Generate Appliance Certificate by CSR    ${retrieve_appliance_cert['commonName']}    ${generate_CSR[0]}    ${remote_server_IP}    ${remote_server_cred}
    Log    ${generate_appliance_cert}
    Set Global Variable    ${all_related_certs}    ${generate_appliance_cert}
    Fusion Api Logout Appliance

Check the Latest Cert Status And Clean EVN
    [Documentation]    Check the latest cert status
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}
    Log    \n-Reset the certificate validation configuration as default if it changed    console=yes
    ${resp} =  Run Keyword And Return Status    Check certificate validation configuration as expected    ${check_validation_body2}
    Run Keyword If    ${resp}!=${True}    Update Certificate Validation Configuration    ${validation_body2}
    Fusion Api Logout Appliance

    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_cred}

    Log    \n-Check the latest cert status    console=yes
    Wait Until Keyword Succeeds    2min    5    Fusion Api Get Certificate Status

    Log    \n-Remove CRL file for ca signed appliance cert    console=yes
    Remove File    ${CURDIR}/appliance_cert.crl
    Remove File    ${CURDIR}/rootcrl_cert.crl

    Log    \n-Clean the test EVN in the remote server
    Clean EVN in Linux    ${remote_server_IP}    ${remote_server_cred}
    Fusion Api Logout Appliance

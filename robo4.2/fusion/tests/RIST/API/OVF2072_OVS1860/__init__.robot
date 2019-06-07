*** Settings ***
Resource             ../Fusion_Env_Setup/keywords.txt
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ../global_variables.robot
Resource             ./keywords.txt
Variables            ${CURDIR}\\${DATA_FILE}

Suite Setup     Precondition Setup
Suite Teardown  Clear Setup

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${rootca_uri}                   /rest/certificates/ca/testca1

*** Keywords ***
Precondition Setup
    [Documentation]  Setup environment for 2FA API test: add Active Directory with SA binding type, enable 2FA flag.
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-Add root CA certificate to OV    console=yes
    Import rootca certificate    ${ca_cert_body}    ${rootca_uri}

    Log    \n-fetching generated CRL files from ssh server ...    console=true
    Fetching generated CRL files from ssh server    ${SSH_SERVER}    ${SSH_USERNAME}    ${SSH_PASSWD}

    Fusion Api Logout Appliance

Clear Setup
    [Documentation]  clean up environment for 2FA API test: disable 2FA flag, delete Active Directory with SA binding type, and remove root CA.
    Set Log Level           TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    \n-running shell file on ssh server to clean up environment...    console=true
    run ssh cmd  ${SSH_SERVER}  ${SSH_USERNAME}  ${SSH_PASSWD}  ${ROOT_DIR}/${CLEANUP_SH} ${APPLIANCE_IP}

    Log    Remove the ca by alias name    console=True
    Run Keyword And Ignore Error    Remove CA By Allias Name    ${CA1_ALIASNAME}

    Log    Remove crl files after tests    console=true
    ${crl_files}=    OperatingSystem.List Files In Directory  path=${CURDIR}  pattern=*.crl  absolute=${True}
    OperatingSystem.Remove Files   @{crl_files}

    Fusion Api Logout Appliance
*** Settings ***
Resource        ../Fusion_Env_Setup/keywords.txt
Resource        ./keywords.txt
Variables       ${DATA_FILE}

Suite Setup  Setup ENV Before OVF442 Test cases

Suite Teardown  Enable SSH Access On Applaince

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird15
${Add_LE}                       true
${Add_Storage}                  false

*** Keywords ***
Setup ENV Before OVF442 Test cases
    [Documentation]    Setup environment for OVF442
    Set Log Level      TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Ensure Appliance is HA Cluster
    Ensure CIM Can be Ping Through
    Refactor DTO If CIM1 Is Standby Node

    Edit Ssh Access    ${enable_ssh_body}

    Config CIM iLo    ${APPLIANCE_IP}    ${MAINTENANCE_CREDENTIALS}
    Sleep    10s
    Ensure CIM Can be Ping Through

Enable SSH Access On Applaince
    [Documentation]  Enable ssh access
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Edit Ssh Access    ${enable_ssh_body}
    Fusion Api Logout Appliance
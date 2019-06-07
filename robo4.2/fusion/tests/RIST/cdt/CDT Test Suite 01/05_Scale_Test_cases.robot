*** Settings ***
Library             Collections
Resource            ../resource.txt
Resource            ../../../../Resources/api/settings/appliance_networking.txt
Documentation       CDT Backup Test Cases.
Suite Setup         Setup for Backup_Restore
Suite Teardown      Backup_Restore Execution PostConditions

# Setup\Teardown for ALL test cases
Test Setup      Test Setup
Test Teardown   Test Teardown

*** Test Cases ***

Validate Backup And Restore
    [Documentation]    Perform Backup and Restore test on OV and validate
    ...                critical alerts, health status and state of managed resources
    [Tags]    backup

    ${failcount} =    Set Variable      ${0}
    ${before_bkp_alerts} =    Get Active Alert List
    Perform Topology Validations        Before Taking Backup
    ${backup_filename} =    Create Backup And Download To Local

    Install Oneview Using Nuvo
    Add Remote Enclosure Setup    ${FLM_IPv6}
    Wait For Resources To Reach Desired State     True
    Perform Topology Validations    After OV Reimage Using Nuvo
    ${after_ov_install_alerts} =    Get Active Alert List

    ${restore_start_time} =    Perform Restore Via Maintenance Console    ${backup_filename}    ${restore_timeout}    ${restore_poll_interval}
    ${count} =    Enclosure Refresh Tasks Should Be OK    ${restore_start_time}
    ${failcount} =    Evaluate    ${failcount}+${count}

    # Remote support enablement validation for all servers
    ${status} =    Run Keyword And Return Status    Wait Until Servers Reached State
    ...            Enabled    60 sec   10 sec    stateStr=['supportState']
    ${failcount} =    Run Keyword If    '${status}' == 'False'   Evaluate    ${failcount}+1
    ...                         ELSE     Set Variable    ${failcount}

    ${restore_alerts} =    Get Active Alert List   ${restore_start_time}
    ${count} =    Compare And Get Actual Restore Alerts    ${before_bkp_alerts}
    ...                           ${after_ov_install_alerts}    ${restore_alerts}
    ${failcount} =    Evaluate    ${failcount}+${count}
    Run Keyword If    ${failcount}>0    Fail    Restore operation ended up with issues
    ...        ELSE   Log     No errors encountered during Restore operation    console=True

Perform Master Appliance Efuseon
    [Documentation]    Perform Master Appliance Efuseon, Status of Secondary appliance and Cluster IP Pingable test.
    Run Keyword If   "${APPLIANCE_IP}" == "${Null}"   Fail   msg=APPLIANCE_IP was not specified in the command or set in data variable file.
    Efuseon Appliance

Perform Master Appliance Efuseoff
    [Documentation]    Perform Master Appliance Efuseoff, Status of Primary appliance
    Run Keyword If   "${APPLIANCE_IP}" == "${Null}"   Fail   msg=APPLIANCE_IP was not specified in the command or set in data variable file.
    Efuseoff Appliance

Perform Secondary Appliance Efuseon
    [Documentation]    Perform Secondary Appliance Efuseon, Status of Primary appliance and Cluster IP Pingable test.
    Run Keyword If   "${APPLIANCE_IP}" == "${Null}"   Fail   msg=APPLIANCE_IP was not specified in the command or set in data variable file.
    Efuseon Appliance

Perform Secondary Appliance Efuseoff
    [Documentation]    Perform Secondary Appliance Efuseoff, Status of Primary appliance
    Run Keyword If   "${APPLIANCE_IP}" == "${Null}"   Fail   msg=APPLIANCE_IP was not specified in the command or set in data variable file.
    Efuseoff Appliance

*** Keywords ***
Setup for Backup_Restore
    [Documentation]     Pre-conditions for CDT Test Suite to prevent test executions if Setup/Initial Config fails.
    ...                 Initial Configuration Suite should pass.
    ...                 Environment Validation should pass.
    #Should be true      ${initialConfigSuccess}     Initial Configuration failed to complete successfully.
    Validate Environment

Backup_Restore Execution PostConditions
    [Documentation]    Backup_Restore Suite Post execution condition status check
    Set Global variable     ${scaleSuiteSuccess}     ${None}
    Run Keyword If      '${SUITE_STATUS}' == 'PASS'     Set Global variable     ${scaleSuiteSuccess}     ${TRUE}


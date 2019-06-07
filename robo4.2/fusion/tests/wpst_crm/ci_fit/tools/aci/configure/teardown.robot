*** Settings ***
Documentation          This script is to tearddown Cisco APIC config using REST API.
...                    Example: Delete EPGs, Bridge Domains, VRFs, Application Profiles, and Tenants
...                    pybot -d /var/www/html/logs/apic-teardown/Eagle62/ -L TRACE -V ../resources/Eagle62_APIC_multi_data_variable.py teardown.robot

Library                ../../../tests/robustness/resources/robustness-helper.py
Library                ../resources/APICOperations.py
Library                APICOperations
Library                json
Resource               ../resources/common.robot

Suite Setup            Login To APIC And Set Session

*** Variables ***

*** Test cases ***
Delete EPGs
    [Tags]   MINIMAL   EPG   ENDPOINT_GROUPS
    ${TENANTS} =   Get Variable Value   ${TENANTS}
    Delete All EPGs From Tenants In Data File   ${TENANTS}

Delete Bridge Domains
    [Tags]   MINIMAL   BD   BRIDGE_DOMAINS
    ${TENANTS} =   Get Variable Value   ${TENANTS}
    Delete All Bridge Domains From Tenants In Data File   ${TENANTS}

Delete VRFs or Contexts
    [Tags]   MINIMAL   VRF   CONTEXTS
    ${TENANTS} =   Get Variable Value   ${TENANTS}
    Delete All VRFs From Tenants In Data File   ${TENANTS}

Delete Application Profiles
    [Tags]   MINIMAL   PROFILES   APP_PROFILES   APPLICATION_PROFILES
    ${TENANTS} =   Get Variable Value   ${TENANTS}
    Delete All Application Profiles From Tenants In Data File   ${TENANTS}

Delete Tenants
    [Tags]   MINIMAL   TENANTS
    ${TENANTS} =   Get Variable Value   ${TENANTS}
    Delete All Tenants   ${TENANTS}

*** Keywords ***


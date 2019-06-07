*** Settings ***
Resource        ./keywords.txt
Variables       ${DATA_FILE}

Suite Setup     Precondition Setup
Suite Teardown  Clear Environment After Test

*** Variables ***
${APPLIANCE_IP}    ${None}

*** Keywords ***
Precondition Setup
    [Documentation]  The precondition Setup
    Set Log Level           TRACE
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Run Keyword And Ignore Error    Remove All FC Networks
    Run Keyword And Ignore Error    Remove All FCoE Networks
    Run Keyword And Ignore Error    Remove ALL Storage Systems Async
    Run Keyword And Ignore Error    Remove ALL San Managers Async

Clear Environment After Test
    [Documentation]  Clear Environment After Test
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Run Keyword And Ignore Error    Remove All DL Server Hardware Async
    Run Keyword And Ignore Error    Delete Power Device By Name Async    ${IPDU_SERVER_CA_SIGN_PDU}
    Run Keyword And Ignore Error    Remove ALL Storage Systems Async
    Run Keyword And Ignore Error    Remove ALL San Managers Async
    Run Keyword And Ignore Error    Remove All Directories Async
    Run Keyword And Ignore Error    Remove All Repositories

    Run Keyword And Ignore Error    Remove CA By Allias Name    ${ldap_root_ca}
    Run Keyword And Ignore Error    Remove CA By Allias Name    ${ldap_intermedia_ca}
    Run Keyword And Ignore Error    Remove CA By Allias Name    ${ad_root_ca}

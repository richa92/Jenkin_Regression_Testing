*** Settings ***
Resource    ./keywords.txt
Variables   ${DATA_FILE}

Suite Setup  Precondition Setup
Suite Teardown  Clear Environment After Test

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one

*** Keywords ***
Precondition Setup
    [Documentation]  The precondition Setup
    Set Log Level           TRACE

Clear Environment After Test
    [Documentation]  Clear Environment After Test
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Run Keyword And Ignore Error    Delete Power Device By Name Async    ${IPDU_SERVER_CA_SIGN_PDU}
    Run Keyword And Ignore Error    Remove All DL Server Hardware Async

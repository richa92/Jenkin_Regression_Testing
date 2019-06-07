*** Settings ***
Documentation   Remove all LE, EG and LIGs to prepare for next team usage.

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Remove LEs.
    [Documentation]    LE, EG and LIGs.
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    Remove All LEs Async   force=${True}    timeout=1800    interval=10

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove EG.
    [Documentation]    Remove EGs
    Remove All Enclosure Groups
    Sleep    30s    SAS LIGS still associated to

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove LIGs.
    [Documentation]    Remove LIGs
    Remove All SAS LIGs
    Remove All LIGs

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
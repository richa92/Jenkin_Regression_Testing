*** Settings ***
Documentation   Remove all Networks to prepare for next team usage.

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Remove Network Sets
    [Documentation]    Remove Network Sets
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    Remove All Network Sets

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove Ethernet Networks
    [Documentation]    Remove Ethernet  Networks
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    Remove All Ethernet Networks

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove FC Networks
    [Documentation]    Remove FCNetworks
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    Remove All FC Networks

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove FCoE Networks
    [Documentation]    Remove FCoE Networks
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    Remove All FCoE Networks

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors
*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
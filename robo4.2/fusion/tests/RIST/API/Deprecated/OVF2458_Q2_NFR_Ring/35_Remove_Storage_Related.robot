*** Settings ***
Documentation   Remove all Storage Related Resources

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Remove Storage Systems
    [Documentation]    Remove Storage Systems
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    Remove ALL Storage Systems Async

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove SAN Managers
    [Documentation]    Remove SAN Managers
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    Remove ALL San Managers Async

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove Storage Volumes
    [Documentation]    Remove Storage Volumes
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    ${resplist} =    Remove ALL Storage Volumes Async     param=?suppressDeviceUpdates=true
    Wait For Task2    ${resplist}    timeout=60    interval=5

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
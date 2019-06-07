*** Settings ***
Documentation   Remove all server profiles.  Should be done to cleanup 3Par (San Storage)

Suite Setup       Fusion Api Login Appliance           ${APPLIANCE_IP}         ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

Resource        ../../../../Resources/api/fusion_api_resource.txt

*** Test Cases ***
OVF2458 Remove All Profiles.
    [Documentation]    Remove All Profiles
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}

    ${tasklist} =    Remove All Server Profiles Async
    Wait For Task2    ${tasklist}    timeout=20m    interval=30

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

OVF2458 Remove All Server Profile Templates.
    [Documentation]    Remove All SPTs
    [Setup]            Run Keyword and Ignore Error    Write To ciDebug Log

    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

    [Teardown]         Run Keyword If    '${TEST_STATUS}' == 'FAIL'   Get Errors

*** Keywords ***
Get Errors
    [Documentation]    Get Errors
    ${ERRORS} =        Run Keyword and Ignore Error    Get from ciDebug Log     ${TEST_NAME}
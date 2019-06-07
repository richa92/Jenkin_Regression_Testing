*** Settings ***
Documentation      Tests to get Support Dump
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

GET SUPPORT DUMP
    [Tags]    SD
    [Documentation]        CGET SUPPORT DUMP for OneView Appliance
    ${dumpUri}=  Create Support Dump Batch  ${support_dump}  ${VERIFY}
    Run Keyword If    '${dumpUri}' == '${null}'    FAIL    Failed to create support dump
    Downloading Support Dump  ${dumpUri}  ${VERIFY}
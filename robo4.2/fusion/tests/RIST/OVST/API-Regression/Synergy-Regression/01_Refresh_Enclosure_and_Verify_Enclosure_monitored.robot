*** Settings ***
Documentation                   Refresh Enclosure and Verify Monitored Enclosure
Resource                        resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Refresh Enclosure
    [Documentation]        Refresh Enclosure
    [Tags]      REFRESH
    ${responses}=  Refresh Enclosures Async   ${monitored_enclosures}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=5000    interval=20

Verify Enclosure
    [Documentation]        Verify Enclosure
    [Tags]      VERIFY
    Verify Resources for List    ${expected_monitored_enclosures}

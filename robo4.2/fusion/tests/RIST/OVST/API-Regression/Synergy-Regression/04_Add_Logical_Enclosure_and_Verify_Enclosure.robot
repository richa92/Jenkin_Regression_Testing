*** Settings ***
Documentation                   Add Logical Enclosures to OneView and Verify
Resource                        resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***
Add Logical Enclosure
    [Documentation]        Add Logical Enclosure to OneView
    [Tags]      ADDLE
    Add Logical Enclosure from lists    ${logical_enclosure}
    Verify Resources for List           ${expected_logical_enclosure}

Verify Enclosure
    [Documentation]        Verify Logical Enclosure
    [Tags]      VERIFY
    Verify Resources for List    ${configured_enclosures}

Refresh Enclosure
    [Documentation]        Refresh Enclosure
    [Tags]      REFRESH
    ${responses}=  Refresh Enclosures Async   ${configured_enclosures}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=5000    interval=20

Verify Enclosure After Refresh
    [Documentation]        Verify Enclosure After Refresh
    [Tags]      VERIFY
    Verify Resources for List    ${configured_enclosures}

*** Settings ***
Documentation    Tests to rename Enclosures
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Rename All Enclosures
    [Tags]    RENAME    T-BIRD
    [Documentation]        Rename Enclosures
    ${responses}=  Edit Enclosure from List    ${encl_update}
    Run Keyword for List with kwargs  ${responses}  Wait For Task2   timeout=500
    Verify Resources for List  ${expected_enclosure}
*** Settings ***
Documentation
...     This Test Suite uses AD Storage Group User credentials for Storage Tests.
...     Test Data is defined in Python Data Variable file.
...     TAGS:                      SETUP
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${ad_storage_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add Shared Storage Volumes
    [Tags]    SETUP  SV  T-BIRD  C7000
    [Documentation]        Add Shared Storage Volumes to OneView
    ${responses}=  Add Storage Volumes Async  ${new_volumes_add_system_validation}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_new_volumes_add_system_validation}

Update Storage Volumes
    [Tags]    EXECUTION  UPDATE-SV  T-BIRD  C7000
    [Documentation]        Edit Storage VOLUMES to OneView
    ${responses}=  Edit Storage Volumes Async  ${edit_storage_volume_system_validations}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}
    Verify Resources for List  ${expected_edit_storage_volumes_system_validation}
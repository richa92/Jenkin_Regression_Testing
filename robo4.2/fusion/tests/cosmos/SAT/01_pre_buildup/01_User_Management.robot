*** Settings ***
Documentation
...     This Test Suite uses Administrator credentials for AD Tests.
...     Test Data is defined in Python Data Variable file.
Resource                ../resource.txt
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Add Active Directory Servers
    [Documentation]     Add Active Directory Server To OV By Administrator
    [Tags]   ADD-AD  T-BIRD  C7000
    Regression Test Setup     ${admin_credentials}
    Run Keyword If  ${ad} is not ${null}     Add Active Directory Async  ${ad}  ${VERIFY}  ${expected_ad}

Add Active Directory Groups
    [Documentation]     Add Active Directory group and assign role.
    [TAGS]    ADD-AD-GRP  T-BIRD  C7000
    Regression Test Setup     ${admin_credentials}
    Run Keyword If  ${adgroup} is not ${null}     Add Active Directory Group And Assign Role  ${adgrp}    ${VERIFY}  ${expected_adgrp}

Active Directory Groups Associated With Users Should Able To Login
    [Documentation]    Active Directory Groups Associated With Users Should Able To Login
    [TAGS]   LOGIN-AD-USERS  T-BIRD  C7000
    Run Keyword If  ${adgroup} is not ${null}    All Active Directory Group Users Should Be Able To Login    ${adgroup}

Login With Backup Active Directory Group Associated With Backup User And Create Backup
    [Documentation]    Login with Backup user. Create backup and validate.
    [Tags]    BACKUP-USER  T-BIRD  C7000
    Regression Test Setup     ${ad_backup_credentials}
    Create Backup
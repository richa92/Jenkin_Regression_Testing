*** Setting ***
Documentation     UI related test scenarios for supportibility team .
Resource          UiResource.robot
Suite Setup       Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers

*** Test Cases ***

Upload and apply fixme on appliance
    [Documentation]    Login to the appliance and uploads and apply fixme.bin file
    [Tags]    uploadfixme
    Upload fixme

Audit Log should be present for applying fixme
    [Documentation]    Verifies audit log to check whether the log is created for applying fixme
    [Tags]     auditfix
    Audit Log should contain fixme log

Fixme Alert should be present in activity page
    [Documentation]    Verifies activity page to check fixme state
    Activity Page Should Contain Fixme Alert

Check whether the fix is applied or not in the appliance
    [Documentation]    To Validate the weather the fix is applied or not in the appliance
    Fix Should Be Applied

Check fixmeinstallog contents against update log
    [Documentation]    compares log from updatelog and fixmeinstall log
    Fixme and Update logs Should Be Equal

Download fixmeinstallation details from UI and validate it contents
    [Documentation]    compares downloaded log with update log
    [Tags]     fixme
    Download fixmeinstallation details and validate it contents

Cidebug log check for Backup Task
    [Documentation]    Enable diagnostic flag , initiate backup , Download cidebug log using UI and search for backup related entry field in log file
    [Tags]    cidebug
    CiDebug download and check for backup entry

Audit log check for Support Dump
    [Documentation]    Verifies the entry for Support-Dump Creation/Failure in Audit Log
    [Tags]    audit
    Download audit log for Support Dump creation in appliance


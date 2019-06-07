*** Setting ***
Documentation     OOPS / ERROR page UI related test scenarios for supportibility team.
Resource          OopsResource.robot
Suite Setup       Load Test Data and Open Browser
Suite Teardown    Logout And Close All Browsers

*** Test Cases ***

Change Appliance state to OOPS
    [Documentation]    OneView state change from OK to ERROR
    [Tags]    Induce-Error-OV
    Update Controller State    ${controller_state}    ${controller_state_msg}
    Reload page

OOPS page Details link contents check
    [Documentation]    Checks and Validate Details link elements in UI and print the output
    [Tags]    Oops-Error-Summary
    Check Error Summary In OOPS Page    ${TestData.users[0].name}    ${TestData.users[0].password}

Create Support Dump in OOPS page
    [Documentation]    Validates the Support dump elemsnts and creation on OOPS page
    [Tags]    Oops-SD
    Support dump creation in OOPS page    ${TestData.users[0].name}    ${TestData.users[0].password}

Restart appliance from OOPS page
    [Documentation]    Restarts appliance from oops page and validates the health after restart finishes
    [Tags]    Oops-Reboot
    Check Restart Link in Oops Page
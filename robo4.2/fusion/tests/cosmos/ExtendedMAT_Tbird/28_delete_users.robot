*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Users From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Test Cases ***
Delete Users as an Administrator
    Log into Fusion appliance as Administrator
    ${status}=          Fusion UI Remove User   @{TestData.users}
    Should Be True      ${status}    Failed to remove user

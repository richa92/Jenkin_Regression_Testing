*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Storage System From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   storage

*** Test Cases ***
Delete Storage System as an Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=          Fusion UI Remove Storage Systems    @{TestData.storagesystems}
    Should Be True      ${status}   Error Removing Storage Systems

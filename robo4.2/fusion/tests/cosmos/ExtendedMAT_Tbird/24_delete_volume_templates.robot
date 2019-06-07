*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Storage Templates From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   storage

*** Test Cases ***
Delete Storage Templates as an Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=          Fusion UI delete storage volume template    @{TestData.storagevts}
    Should Be True      ${status}   Failed to delete storage templates

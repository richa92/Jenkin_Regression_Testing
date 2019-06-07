*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Network Sets From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   network

*** Test Cases ***
Delete Network Sets as Network Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=        Fusion UI Delete Network Set    @{TestData.networksets}
    Should Be True    ${status}   Failed to delete network set

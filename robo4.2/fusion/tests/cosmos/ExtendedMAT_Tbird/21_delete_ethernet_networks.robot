*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Ethernet Network From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   network

*** Test Cases ***
Delete Ethernet Networks as Network Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=        Fusion UI delete ethernet network   @{TestData.networks}
    Should Be True    ${status}   Failed to delete ethernet network

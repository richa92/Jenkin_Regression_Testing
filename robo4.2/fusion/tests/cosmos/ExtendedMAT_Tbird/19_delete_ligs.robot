*** Settings ***
Resource        Tbird-resource.txt
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   network

*** Test Cases ***
Delete LIGs as Network Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=       Fusion UI delete logical interconnect group     @{TestData.ligs}
    Should Be True   ${status}   Failed to delete logical interconnect group

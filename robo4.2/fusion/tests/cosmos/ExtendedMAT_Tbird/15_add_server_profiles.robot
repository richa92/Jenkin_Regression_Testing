*** Settings ***
Documentation   Add Server Profiles as Server Administrator
Resource        Tbird-resource.txt
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SA}   server

*** Test Cases ***
Add Server Profiles Without Storage as Server Administrator
    Fusion UI Login To Appliance    ${SA}
    ${result}=                      Fusion UI Create Server Profile    @{TestData.profiles}
    Should Be True                  ${result}   Failed to create server profile due to error.

Verify Server Profiles Without Storage as Server Administrator
    Fusion UI Login To Appliance    ${SA}
    ${result1}=                     Fusion UI Verify Server Profile General Info    @{TestData.profiles}
    Should Be True                  ${result1}   Failed to verify server profile general information.
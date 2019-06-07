*** Settings ***
Documentation   Delete Server Profiles as an Administrator
Resource        Tbird-resource.txt
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SA}   server

*** Test Cases ***
Remove Server Profiles Without Storage as an Administrator
    Fusion UI Login To Appliance    ${SA}
    ${status1}=                     Fusion UI delete Server Profile    @{TestData.profiles}
    Should be True                  ${status1}   msg=Failed to delete BL Server profile

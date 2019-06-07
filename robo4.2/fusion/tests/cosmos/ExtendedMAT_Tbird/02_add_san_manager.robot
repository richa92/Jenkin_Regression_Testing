*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add San Manager To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}     Administrator

*** Test Cases ***
Add San Manager as an Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=       Fusion UI Add San Manager   @{TestData.sanmanagers}
    Should Be True   ${status}   msg= Successfully Added A SAN Manager

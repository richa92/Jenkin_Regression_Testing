*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete San Managers From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}     storage

*** Test Cases ***
Delete San Managers as an Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=          Fusion UI Remove San Manager    @{TestData.sanmanagers}
    Should Be True      ${status}                       msg=Failed to Remove SAN Managers

*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Storage Volumes From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   storage

*** Test Cases ***
Delete Storage Volumes as an Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=         fusion ui delete all storage volumes
    Should Be True     ${status}     msg=Failed to remove storage volumes

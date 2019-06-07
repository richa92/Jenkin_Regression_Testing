*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Storage Volumes To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}     storage

*** Test Cases ***
Create Storage Volumes as an Storage Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=                      Fusion UI Create Storage Volumes    @{TestData.storagevolumes}
    Should Be True                  ${status}   msg=Failed to create storage volumes

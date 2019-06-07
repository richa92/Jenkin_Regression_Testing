*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Storage Pools To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}     storage

*** Test Cases ***
Add Storage Pools as an Storage Administrator
    Fusion UI Login To Appliance    ${user}
    ${rc}=                          Fusion Ui Edit Storage Pools     @{TestData.storagepools}
    Should be True                  ${rc}   msg= Failed to add Storage Pools

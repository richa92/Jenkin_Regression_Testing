*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Storage Systems To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${status}   False
${user}     storage

*** Test Cases ***
Add Storage Systems as an Storage Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=         Fusion UI add storage systems   @{TestData.storagesystems}
    Should Be True     ${status}    msg= Successfully added storagesystem

*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Storage Templates To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}     storage

*** Test Cases ***
Add Storage Templates as an Storage Administrator
    Fusion UI Login To Appliance    ${user}
    ${result}=          Fusion UI create storage volume templates   @{TestData.storagevts}
    Should Be True      ${result}

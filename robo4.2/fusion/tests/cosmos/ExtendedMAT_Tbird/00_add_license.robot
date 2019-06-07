*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add License To OneView
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Test Cases ***
Add License as an Administrator
    Log into Fusion appliance as Administrator
    ${Status}=  Fusion UI Add License   @{TestData.licenses}

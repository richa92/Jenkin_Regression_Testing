*** Settings ***
Resource        Tbird-resource.txt
Documentation   Create Support Dump From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Test Cases ***
Create Support Dump as an Administrator
    Log into Fusion appliance as Administrator
    Fusion UI Create Support Dump From Data File  @{TestData.supportdump}
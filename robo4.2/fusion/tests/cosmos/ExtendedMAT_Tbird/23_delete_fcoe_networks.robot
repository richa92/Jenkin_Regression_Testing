*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Fcoe Network From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   network

*** Test Cases ***
Delete Fcoe Networks as Networks Administrator
    Fusion UI Login To Appliance    ${user}
    ${status}=        Fusion UI delete fcoe network     @{TestData.fcoenetworks}
    Should Be True    ${status}   Failed to delete fc network

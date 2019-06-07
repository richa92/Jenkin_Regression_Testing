*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Fcoe Networks To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   network

*** Test Cases ***
Add Fcoe Networks as an Network Administrator
    Fusion UI Login To Appliance    ${user}
    Fusion UI create fcoe network   @{TestData.fcoenetworks}

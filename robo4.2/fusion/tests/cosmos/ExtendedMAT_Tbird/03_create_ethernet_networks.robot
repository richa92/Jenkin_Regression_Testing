*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Ethernet Networks To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}    network

*** Test Cases ***
Create Ethernet Networks as an Network Administrator
    Fusion UI Login To Appliance    ${user}
    ${Status}=                      Fusion UI create ethernet network   @{TestData.networks}
    Should Be True                  ${Status}   msg= Failed to add network

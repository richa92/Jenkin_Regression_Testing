*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add FC Networks To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   network

*** Test Cases ***
Add FC Networks as an Network Administrator
    Fusion UI Login To Appliance    ${user}
    ${Status}=                      Fusion UI create fc network     @{TestData.fcnetworks}
    Should Be True                  ${Status}                       msg= Failed to add network

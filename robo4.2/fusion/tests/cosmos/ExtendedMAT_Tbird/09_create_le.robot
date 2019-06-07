*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Logical Enclosures To OneView Appliance
Test Setup      Run Keywords  Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   server

*** Test Cases ***
Create Logical Enclosures as an Sever Administrator
    Fusion UI Login To Appliance    ${user}
    ${Status}=                      fusion ui create tbird logical enclosure    @{TestData.les}
    Should Be True                  ${Status}   msg=Failed to add LE

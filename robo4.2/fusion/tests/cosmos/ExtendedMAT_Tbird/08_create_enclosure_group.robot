*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Enclosure Groups To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   server

*** Test Cases ***
Create Enclosure Groups as an Sever Administrator
    Fusion UI Login To Appliance    ${user}
    ${Status}=                      fusion ui create tbird enclosure group    @{TestData.encgroups}
    Should Be True                  ${Status}   msg=Failed to add eg

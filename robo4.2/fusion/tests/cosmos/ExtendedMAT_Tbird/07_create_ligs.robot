*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Ligs To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}   network

*** Test Cases ***
Create Ligs as an Network Administrator
    Fusion UI Login To Appliance    ${user}
    ${Status}=                      Fusion UI Create Tbird Logical Interconnect Group   @{TestData.ligs}
    Should Be True                  ${Status}   msg=Failed to add ligs

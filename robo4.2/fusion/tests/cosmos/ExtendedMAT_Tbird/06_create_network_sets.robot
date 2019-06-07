*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Network Sets To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${user}  network

*** Test Cases ***
Add Network Sets as an Network Administrator
    Fusion UI Login To Appliance    ${user}
    ${Status}=                      Fusion UI create network set    @{TestData.networksets}
    Should Be True                  ${Status}                       msg= Failed to add network set


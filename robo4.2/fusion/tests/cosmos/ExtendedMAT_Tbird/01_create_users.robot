*** Settings ***
Resource        Tbird-resource.txt
Documentation   Add Users To OneView Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Test Cases ***
Add Users as an Administrator
    Log into Fusion appliance as Administrator
    ${Status}=       Fusion UI Create User   @{TestData.users}
    Should Be True   ${Status}   msg= Failed to add users

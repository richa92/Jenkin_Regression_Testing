*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Enclosure Group From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SA}   server

*** Test Cases ***
Delete Enclosure Group as an Server Administrator
    Fusion UI Login To Appliance    ${SA}
    ${Status}=       Fusion UI delete enclosure group    @{TestData.encgroups}
    Should Be True   ${status}   Failed to delete enclosure group

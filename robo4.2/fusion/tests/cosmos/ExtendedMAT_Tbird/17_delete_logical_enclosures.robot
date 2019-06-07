*** Settings ***
Resource        Tbird-resource.txt
Documentation   Delete Logical Enclosures From Appliance
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SA}   server

*** Test Cases ***
Delete Logical Enclosures as an Server Administrator
    Fusion UI Login To Appliance    ${SA}
    ${Status}=                      Fusion Ui Delete Logical Enclosure    @{TestData.les}
    Should Be True                  ${Status}   msg=Failed to delete eg

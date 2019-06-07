*** Settings ***
Resource        Tbird-resource.txt
Documentation   Verify Configured Tbird Enclosures
Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Test Cases ***
Verify Configured Tbird Enclosure as an Administrator
    Log into Fusion appliance as Administrator
    ${status}=       Fusion Ui Validate TBird Enclosure Configuration     @{TestData.enclosures_configured.verify}
    Should Be True   ${status}    msg=Failed to verify tbird Configured Enclosures

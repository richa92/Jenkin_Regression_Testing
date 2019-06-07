*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         F136/Regression_data.xml    # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F136p0010-Interconnect page-turn on off UID-check state
    ${status}=              fusion ui turn on interconnect uid      @{TestData.interconnects}
    should be true          ${status}    msg = Fail to set the interconnect status into on - F136p0010.
    Sleep                   10
    ${status}=              fusion ui turn off interconnect uid      @{TestData.interconnects}
    should be true          ${status}    msg = Fail to set the interconnect status into off - F136p0010.

*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         F136/Regression_data.xml    # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F136p0009-Interconnect page-UID on the left of Action-default state is off
    ${status}=              fusion ui validate interconnect uid light off        @{TestData.interconnects}
    should be true          ${status}    msg = Fail to verify the default status of Interconnect - F136p0009.


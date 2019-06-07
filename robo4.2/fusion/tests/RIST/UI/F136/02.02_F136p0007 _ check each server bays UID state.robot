*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         F136/Regression_data.xml    # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F136p0007-serverhardware page-UID on the left of Action-default state is off
    ${status}=              fusion ui validate server uid light off        @{TestData.TbirdServers}
    should be true          ${status}    msg = Fail to verify the default status of ServerHardwares - F136p0007.


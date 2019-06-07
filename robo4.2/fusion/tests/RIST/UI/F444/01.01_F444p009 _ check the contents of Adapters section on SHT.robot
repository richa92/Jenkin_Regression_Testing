*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         ./F444/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F444p009-check the contents of Adapters section on SHT
    ${status}=              fusion ui validate server hardware types page        @{TestData.verifyservertypes}
    should be true          ${status}    msg = Fail to verify the contents of adapters section on SHT - F444p009.


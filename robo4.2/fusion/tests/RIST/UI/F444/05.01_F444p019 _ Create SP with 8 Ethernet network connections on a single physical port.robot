*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         ./F444/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F444p019-Create SP with 8 Ethernet network connections on a single physical port
    ${status}=              fusion ui create server profile        @{TestData.profile8connetions}
    should be true          ${status}    msg = Fail to Create SP with 8 Ethernet network connections on a single physical port - F444p019.


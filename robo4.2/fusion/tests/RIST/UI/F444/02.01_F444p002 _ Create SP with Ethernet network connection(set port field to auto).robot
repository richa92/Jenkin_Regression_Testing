*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}                 ./F444/Regression_data.xml  # Data File Location
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F444p002-Create SP with Ethernet network connection-set port field to auto
    ${status}=              fusion ui create server profile        @{TestData.profileauto}
    should be true          ${status}    msg = Fail to Create SP with Ethernet network connection-set port field to auto - F444p002.


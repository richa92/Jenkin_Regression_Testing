*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         ./F444/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F444p010-Create SP with Ethernet networkset connection-set port field to one port suffixed with-efgh
    ${status}=              fusion ui create server profile        @{TestData.profilenetset}
    should be true          ${status}    msg = Fail to Create SP with Ethernet networkset connection-set port field to one port suffixed with-efgh - F444p010.
    ${status}=              fusion ui delete server profile        @{TestData.profilenetset}
    should be true          ${status}    msg = Fail to Delete SP with Ethernet networkset connection-set port field to one port suffixed with-efgh - F444p010.

*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         ./F444/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F444p021-Delete SP with Ethernet network connection-set port field to one port suffixed with-efgh when blade server is powered off
    ${status}=              fusion ui delete server profile        @{TestData.profile8connetions}
    should be true          ${status}    msg = Fail to Delete SP with Ethernet network connection-set port field to one port suffixed with-efgh when blade server is powered off - F444p021.

*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         ./F444/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F444p005-Edit SP with Ethernet network connection-set port field to one port suffixed with-efgh
    ${status}=              fusion ui edit server profile        @{TestData.profilewithefghedit}
    should be true          ${status}    msg = Fail to edit SP with Ethernet network connection-set port field to one port suffixed with-efgh - F444p005.


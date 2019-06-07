*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}                 ./F444/Regression_data.xml  # Data File Location
${ApplianceUrl}             https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F444p022-Create SPT with Ethernet network connection-set port field to one port suffixed with -efgh
    ${status}=              fusion ui create server profile template        @{TestData.profiletemplate}
    should be true          ${status}    msg = Fail to Create SPT with Ethernet network connection-F444p022.
    ${ret}=                 fusion ui delete server profile template        @{TestData.profiletemplate}
    should be true          ${ret}       msg = Fail to delete SPT with Ethernet network connection-F444p022.




*** Settings ***
Resource    ../resource.txt
Resource    ./keywords.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         F136/Regression_data.xml    # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F136p0006-Serverhareware page-turn on off UID-check state
    ${status}=              fusion ui turn on server uid      @{TestData.TbirdServers}
    should be true          ${status}    msg = Fail to set the server status into on - F136p0006.
    ${status}=              fusion ui turn off server uid      @{TestData.TbirdServers}
    should be true          ${status}    msg = Fail to set the server status into off - F136p0006.


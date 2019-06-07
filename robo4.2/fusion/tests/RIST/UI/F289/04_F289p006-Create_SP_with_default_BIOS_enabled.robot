*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles

*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
As an Administrator I want to create SP with default BIOS enabled
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F289P006}
    should be true   ${Result}   msg=Failed to create Server Profile



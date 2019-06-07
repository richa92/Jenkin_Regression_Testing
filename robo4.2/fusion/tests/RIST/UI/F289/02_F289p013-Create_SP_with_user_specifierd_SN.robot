*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles

*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
As an Administrator I want to create SP with user specifierd SN
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F289P013}
    should be true   ${Result}   msg=Failed to create Server Profile

    ${Result} =      Fusion UI Verify Server Profile Advanced Info   @{TestData.F289P013}
    should be true   ${Result}    msg=Failed to verify Server Profile Advanced Info

    ${Result} =      Fusion UI Verify Server Profile General Info    @{TestData.F289P013}
    should be true   ${Result}    msg=Failed to verify Server Profile user specified SN from General Info

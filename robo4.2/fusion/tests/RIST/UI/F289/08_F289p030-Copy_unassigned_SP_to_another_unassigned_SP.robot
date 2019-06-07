*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles

*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url

*** Test Cases ***
As an Administrator I want to copy unassigned SP to another unassigned SP
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F289P030.Create}
    should be true   ${Result}   msg=Failed to create Server Profile

    ${Result} =      Fusion UI Copy Server Profile  @{TestData.F289P030.Copy}
    should be true   ${Result}   msg=Failed to copy unassigned Server Profile to another unassigned

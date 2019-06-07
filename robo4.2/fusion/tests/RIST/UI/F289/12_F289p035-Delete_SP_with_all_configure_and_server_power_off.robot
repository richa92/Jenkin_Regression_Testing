*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser

*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
As an Administrator I want to delete SP with all configure and server power off
    ${Result} =      Fusion UI Create Server Profile     @{TestData.F289P035.Create}
    should be true   ${Result}   msg=Failed to create Server Profile

    ${Result} =      Fusion UI Delete Server Profile  @{TestData.F289P035.Delete}
    should be true   ${Result}  msg=Failed to delete Server Profile

*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles

*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
As an Administrator I want to create SP with default BIOS enable,then disable
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F289P017.Create}
    should be true   ${Result}   msg=Failed to create Server Profile

    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F289P017.Edit}
    should be true   ${Result}   msg=Failed to edit Server Profiles


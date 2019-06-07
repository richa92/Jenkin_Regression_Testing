*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url



*** Test Cases ***
As an Administrator I want to power on server from SP page
    ${Result} =      Fusion UI Create Server Profile     @{TestData.F289P031}
    should be true   ${Result}   msg=Failed to create Server Profile

    ${Result} =      Fusion UI Power On Server Profile   @{TestData.F289P031}
    should be true   ${Result}   msg=Failed to power on Server Profile


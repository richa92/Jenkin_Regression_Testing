*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
SPECp005 - Create unassign SP with connection port none, auto or specified(auto,specified were covered by other case)
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F114005}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114005}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info

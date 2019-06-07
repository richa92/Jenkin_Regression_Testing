*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
SPECp002 - Create SP with network connection and set port to auto
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F114015.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =      Fusion UI Verify Server Profile Connections Info  @{TestData.F114015.Create}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info
    ${Result} =      Fusion UI Copy Server Profile  @{TestData.F114015.Copy}
    should be true   ${Result}   msg=Failed to copy unassigned Server Profile to real hardware


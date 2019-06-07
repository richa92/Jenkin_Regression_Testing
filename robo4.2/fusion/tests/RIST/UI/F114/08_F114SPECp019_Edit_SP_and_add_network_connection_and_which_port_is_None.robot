*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
SPECp019_Edit SP and add network connection and which port is None and SPECp024_Edit SP and add network connection and set port to None
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F114019.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F114019.Edit}
    should be true   ${Result}   msg=Failed to edit Server Profiles
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114019.Edit}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info

*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
SPECp001 - check VF field and default value on SP page
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F114001.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114001.Create}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info
    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F114001.Editsp}
    should be true   ${Result}   msg=Failed to edit Server Profiles
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114001.Editsp}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info
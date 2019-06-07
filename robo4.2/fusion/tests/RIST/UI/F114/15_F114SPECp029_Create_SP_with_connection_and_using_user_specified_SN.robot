*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
SPECp029 - Create SP with connection and using user-specified SN
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F114029}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =      Fusion UI Verify Server Profile Advanced Info   @{TestData.F114029}
    should be true   ${Result}    msg=Failed to verify Server Profile Advanced Info
    ${Result} =      Fusion UI Verify Server Profile General Info    @{TestData.F114029}
    should be true   ${Result}    msg=Failed to verify Server Profile user specified SN from General Info
     ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114029}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info

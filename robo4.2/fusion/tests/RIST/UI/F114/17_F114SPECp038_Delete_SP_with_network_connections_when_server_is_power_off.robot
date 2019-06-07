*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
SPECp038 - Delete SP with network connections when server is power off
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F114038.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114038.Create}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info
    ${Result} =      Fusion UI Delete Server Profile  @{TestData.F114038.Delete}
    should be true   ${Result}  msg=Failed to delete Server Profile

*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F353/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
F353p003_Create_BlackBird_SP(HPE Synergy 480 Gen9)
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F353P003.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =      Fusion UI Verify Server Profile Advanced Info   @{TestData.F353P003.Create}
    should be true   ${Result}    msg=Failed to verify Server Profile Advanced Info
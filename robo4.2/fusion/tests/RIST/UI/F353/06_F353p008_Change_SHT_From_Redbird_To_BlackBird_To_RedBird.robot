*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F353/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
F353p008_Change_SHT_From_Redbird_To_BlackBird_To_RedBird
     ${Result} =      Fusion UI Create Server Profile  @{TestData.F353P002.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =      Fusion UI Verify Server Profile Advanced Info   @{TestData.F353P002.Create}
    should be true   ${Result}    msg=Failed to verify Server Profile Advanced Info
    ${Result} =      Fusion UI Verify Server Profile General Info    @{TestData.F353P002.Create}
    should be true   ${Result}    msg=Failed to verify Server Profile from General Info
    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F353P002.Edit_blackbird}
    should be true   ${Result}   msg=Failed to edit Server Profiles
    ${Result} =      Fusion UI Verify Server Profile Advanced Info   @{TestData.F353P002.Verify_blackbird}
    should be true   ${Result}    msg=Failed to verify Server Profile Advanced Info
    ${Result} =      Fusion UI Verify Server Profile General Info    @{TestData.F353P002.Verify_blackbird}
    should be true   ${Result}    msg=Failed to verify Server Profile from General Info
    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F353P002.Edit_redbird}
    should be true   ${Result}   msg=Failed to edit Server Profiles
    ${Result} =      Fusion UI Verify Server Profile Advanced Info   @{TestData.F353P002.Verify_redbird}
    should be true   ${Result}    msg=Failed to verify Server Profile Advanced Info
    ${Result} =      Fusion UI Verify Server Profile General Info    @{TestData.F353P002.Verify_redbird}
    should be true   ${Result}    msg=Failed to verify Server Profile from General Info




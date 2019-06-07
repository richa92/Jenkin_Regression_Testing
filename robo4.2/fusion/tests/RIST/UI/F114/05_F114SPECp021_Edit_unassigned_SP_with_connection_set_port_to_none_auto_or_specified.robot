*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
 SPECp021_Edit unassigned SP with connection set port to none, auto or specified
    ${Result} =      Fusion UI Create Server Profile  @{TestData.F114021.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114021.Create}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info
    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F114021.EditAuto}
    should be true   ${Result}   msg=Failed to edit Server Profiles
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114021.EditAuto}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info
    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F114021.Editspecific}
    should be true   ${Result}   msg=Failed to edit Server Profiles
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114021.Editspecific}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info
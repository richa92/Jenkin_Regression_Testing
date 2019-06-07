*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F114/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
SPECp027 - Edit SP and add internal ethernet connection
   ${Result} =      Fusion UI Create Server Profile  @{TestData.F114027.Create}
    should be true   ${Result}   msg=Failed to create Server Profile
    ${Result} =      Fusion UI Edit Server Profile   @{TestData.F114027.Edit}
    should be true   ${Result}   msg=Failed to edit Server Profiles
    ${Result} =     Fusion UI Verify Server Profile Connections Info  @{TestData.F114027.Edit}
    should be true     ${Result}    msg=Failed to verify Server Profile connections info

*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt
Resource    ../../../../Resources/api/fusion_api_resource.txt
Variables   ./Regression_Data.py


Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${DataFile}         F289/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url
${post_state}       IN_POST_DISCOVERY_COMPLETE|FINISHED_POST

*** Test Cases ***
As an Administrator I want to power off server from SP page
    ${Result} =      Fusion UI Create Server Profile     @{TestData.F289P032.Create}
    should be true   ${Result}   msg=Failed to create Server Profile

    ${Result} =      Fusion UI Power On Server Profile   @{TestData.F289P032.Create}
    should be true   ${Result}   msg=Failed to power on Server Profile

    Log To Console And Logfile      \nPOST check to make sure POST is finished
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Wait for Server to reach POST State		 ${TestData.F289P032.Create[0].server}       ${post_state}

    ${Result} =      Fusion UI Power Off Server Profile  @{TestData.F289P032.Create}
    should be true   ${Result}   msg=Failed to power off by Server Profile in Momentary Press way

    ${Result} =      Fusion UI Power On Server Profile  @{TestData.F289P032.Create}
    should be true   ${Result}   msg=Failed to power on by Server Profile

    Log To Console And Logfile      \nPOST check to make sure POST is finished
    Wait for Server to reach POST State		 ${TestData.F289P032.Create[0].server}      ${post_state}

    ${Result} =      Fusion UI Power Off Server Profile  @{TestData.F289P032.MomentaryPress}
    should be true   ${Result}   msg=Failed to power off by Profile in Press and Hold way


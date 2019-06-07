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
As an Administrator I want to reset server from SP page
    ${Result} =      Fusion UI Create Server Profile     @{TestData.F289P033}
    should be true   ${Result}   msg=Failed to create Server Profile

    ${Result} =      Fusion UI Power On Server Profile  @{TestData.F289P033}
    should be true   ${Result}   msg=Failed to power on Server Profile

    ${Result} =      Fusion UI Reset Server Profile  @{TestData.F289P033}
    should be true   ${Result}   msg=Failed to reser Server Profile

    Log To Console And Logfile      \nPOST check to make sure POST is finished
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Wait for Server to reach POST State		 ${TestData.F289P033[0].server}      ${post_state}

    ${Result} =      Fusion UI Cold Boot Server Profile  @{TestData.F289P033}
    should be true   ${Result}   msg=Failed to cold boot Server Profiles


*** Settings ***
Documentation  Validation of server profile creation when connection 1 is configured to Primary boot - with Managed volume Private Volume with OS.

Resource        ../resource.txt
Resource        ./keyword.txt
Resource        ../../../../Resources/api/fusion_api_resource.txt
Variables       ./Regression_Data.py

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear Profile and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url
${post_state}       IN_POST_DISCOVERY_COMPLETE|FINISHED_POST


*** Test Cases ***
Validation of server profile creation when connection 1 is configured to Primary boot - with Managed volume Private Volume with OS.
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F1407UI009.Create}
    Should Be True                      ${rc}   msg=Failed to validate server profile creation when connection 1 is configured to Primary boot - with Private Volume with OS.

    ${rc}                               Fusion UI Verify Server Profile SAN Storage Info    @{TestData.F1407UI009.Create}
    Should Be True                      ${rc}   msg=Failed to verify the private volume in the server profile

    ${rc}                               Fusion UI Verify Server Profile Connections Info    @{TestData.F1407UI009.Create}
    Should Be True                      ${rc}   msg=Failed to verify the connections info in the server profile

#    ${rc}                               Fusion UI Power On Server Profile                   @{TestData.F1407UI009.Create}
#    Should Be True                      ${rc}   msg=Failed to power on server profile

#    Log To Console And Logfile          \nPOST check to make sure POST is finished
#    Fusion Api Login Appliance          ${APPLIANCE_IP}        ${admin_credentials}
#    Wait for Server to reach POST State		 ${TestData.F1407UI009.Create[0].server}       ${post_state}
*** Settings ***
Documentation   Create SP with proper connection and is configured to Primary boot - with Managed Volume - private volume with OS

Resource        ../resource.txt
Resource        ./keyword.txt

Test Setup      Load Test Data and Open Browser and Login
Test Teardown	Clear Profile And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FC/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url
${post_state}       IN_POST_DISCOVERY_COMPLETE|FINISHED_POST


*** Test Cases ***
Create SP with proper connection and is configured to Primary boot - with Managed volume Private volume with OS. Delete the SP and create another SP with same configuration
    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F1407UI020.Create}
    Should Be True                      ${rc}   msg=Failed to create server profile

    ${rc}                               Fusion UI Delete All Appliance Server Profiles
    Should Be True                      ${rc}   msg=Failed to delete server profile

    ${rc}                               Fusion UI Create Server Profile                     @{TestData.F1407UI020.Create}
    Should Be True                      ${rc}   msg=Failed to create server profile with same configuration

#
#    Log To Console And Logfile      \nPOST check to make sure POST is finished
#    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
#    Wait for Server to reach POST State		 ${TestData.F1407UI020.Create[0].server}       ${post_state}
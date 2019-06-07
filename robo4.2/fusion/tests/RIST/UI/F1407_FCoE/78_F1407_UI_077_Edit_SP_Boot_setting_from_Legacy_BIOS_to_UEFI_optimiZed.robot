*** Settings ***
Documentation  Edit Server Profile Boot Setting from Legacy BIOS to UEFI OptimiZed mode

Resource        ../resource.txt
Resource        ./keyword.txt
Resource        ../../../../Resources/api/fusion_api_resource.txt
Variables       ./Regression_Data.py

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause and Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F1407_FCoE/Regression-data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url
${post_state}       IN_POST_DISCOVERY_COMPLETE|FINISHED_POST


*** Test Cases ***
Edit Server Profile Boot Setting from Legacy BIOS to UEFI OptimiZed mode
    ${rc}                               Fusion UI Edit Server Profile                                 @{TestData.F1407UI077.Edit}
    Should Be True                      ${rc}   msg=Failed to Edit Server Profile Boot Setting from Legacy BIOS to UEFI OptimiZed mode

    ${rc}                               Fusion UI Verify Server Profile San Storage Info              @{TestData.F1407UI077.Verify}
    Should Be True                      ${rc}   msg=Failed to verify Server Profile San Storage info

#    ${rc}                               Fusion UI Power On Server Profile                   @{TestData.F1407UI020.Create}
#    Should Be True                      ${rc}   msg=Failed to power on server profile
#
#    Log To Console And Logfile          \nPOST check to make sure POST is finished
#    Fusion Api Login Appliance          ${APPLIANCE_IP}        ${admin_credentials}
#    Wait for Server to reach POST State		 ${TestData.F1407UI020.Create[0].server}       ${post_state}
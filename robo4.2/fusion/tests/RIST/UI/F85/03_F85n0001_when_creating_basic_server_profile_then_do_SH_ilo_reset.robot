*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py

Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Clear server profiles


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F85/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url


*** Test Cases ***
F85n0001_when_creating_basic_server_profile_then_do_SH_ilo_reset.robot

     ${Result} =    Fusion UI create server profile             @{TestData.F85Pn0001.Create}
     should be true            ${Result}    msg=Failed to create server profile

     run keyword and continue on failure   Fusion UI Validate Reset Ilo Was Blocked  ${TestData.F85Pn0001.Create[0].server}    ${unableToResetIloBlockMessage}

     Log To Console And Logfile      \nWait for all server profile to finish
     Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
     Wait For All Server Profile In Normal State

     ${Result} =   Fusion UI Validate Server Profile Status     ok         @{TestData.F85Pn0001.Create}
     should be true            ${Result}    msg=Create server profile failed


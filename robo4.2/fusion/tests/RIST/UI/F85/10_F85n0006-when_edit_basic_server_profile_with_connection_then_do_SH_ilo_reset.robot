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
F85n0006-when_edit_basic_server_profile_with_connection_then_do_SH_ilo_reset

     ${Result} =    Fusion UI create server profile             @{TestData.F85Pn0006.Create}
     should be true            ${Result}    msg=Failed to create server profile
     ${Result} =     Fusion UI Edit Server Profile            @{TestData.F85Pn0006.Edit}
     should be true            ${Result}    msg=Failed to edit server profile
     sleep  120s
     run keyword and continue on failure    Fusion UI Validate Reset Ilo Was Blocked    ${TestData.F85Pn0006.Edit[0].server}    ${unableToResetIloBlockMessage}

     Log To Console And Logfile      \nWait for all server profile to finish
     Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
     Wait For All Server Profile In Normal State

     ${Result} =   Fusion UI Validate Server Profile Status     ok          @{TestData.F85Pn0006.Create}
     should be true            ${Result}    msg=Create server profile failed

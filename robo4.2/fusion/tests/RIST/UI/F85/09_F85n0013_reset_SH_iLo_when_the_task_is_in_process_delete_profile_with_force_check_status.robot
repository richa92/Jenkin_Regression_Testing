*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py


Test Setup      Load Test Data and Open Browser and Login
Test Teardown   Pause And Close Browser


*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.0
${DataFile}         F85/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}    # Appliance Url

*** Test Cases ***
F85n0013_reset_SH_iLo_when_the_task_is_in_process_delete_profile_with_force_check_status

      ${Result} =    Fusion UI create server profile             @{TestData.F85Pn0001.Create}
     should be true            ${Result}    msg=Failed to create server profile

       ${Result} =  Fusion UI Reset Ilo     @{TestData.ResetIloNoWait}
       should be true            ${Result}    msg=Failed to reset ilo for server hardware

      ${Result} =      Fusion UI Delete Server Profile  @{TestData.F85Pn0001.Delete}
      should be true   ${Result}  msg=Failed to delete Server Profile


       Log To Console And Logfile      \nWait for all server hardware to finish to keep the following test without gap
       Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
       Wait For ALL Servers Complete Refresh









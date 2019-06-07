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
F85n0009-when reset ilo, create server profile on this SH

       ${Result} =  Fusion UI Reset Ilo    @{TestData.ResetIloNoWait}
       should be true            ${Result}    msg=Failed to reset ilo for server hardware

       run keyword and expect error       ${TestData.Message[0].SP_error_msg}    Fusion UI create server profile         @{TestData.F85Pn0005.Create}

       Log To Console And Logfile      \nWait for all server hardware to finish to keep the following test without gap
       Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
       Wait For ALL Servers Complete Refresh







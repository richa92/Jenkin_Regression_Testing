*** Settings ***
Resource    ../resource.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py

Test Setup      Load Test Data and Open Browser Then Login
Test Teardown   Remove Profiles and Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         F1236/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Test Cases ***
F1236UIp010  update DL Gen9 server firmware from server profiles succeed with iLO FW 2.30 using Firmware Only
    Update Server ILO Firmware      ${GEN9DL230Server}
    ${rc} =   Fusion UI Create Server Profile      @{TestData.GEN9DLProfile}
    Should Be True                      ${rc}   msg=Some server profile cannot be created


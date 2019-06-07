*** Settings ***
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt

Suite Setup  Setup ENV Before F178 Test cases


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird13
${Add_LE}                       true
${Add_Storage}                  false
${SELENIUM_TIMEOUT}             5.0
${SELENIUM_IMPLICIT_WAIT}       0.00
${DataFile}                     F178/Regression_data.xml  # Data File Location
${ApplianceUrl}                 https://${APPLIANCE_IP}     # Appliance Url

*** Keywords ***
Setup ENV Before F178 Test cases
    Set Log Level    TRACE
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}
    Remove All Firmware Bundles
    Load Test Data and Open Browser Then Login and Add SPP
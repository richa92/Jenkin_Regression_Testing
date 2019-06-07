*** Settings ***
Resource    ../resource.txt
Resource    ../../API/Fusion_Env_Setup/keywords.txt
Resource    ./../../../../Resources/api/fusion_api_resource.txt

Test Setup      Load Test Data and Open Browser
Test Teardown   Pause And Close Browser

*** Variables ***
${SELENIUM_TIMEOUT}             5.0
${SELENIUM_IMPLICIT_WAIT}       0.00
${DataFile}                     UpdateLEFirmware/Regression_data.xml  # Data File Location
${ApplianceUrl}                 https://${APPLIANCE_IP}     # Appliance Url
${Team_Name}                    SHQA
${admin_credentials}            ${TBirdEnvSetup.${Team_Name}.Common.admin_credentials}
${Ring}                         TBird13
${Add_LE}                       true
${Add_Storage}                  false

*** Test Cases ***
Update LE Firmware To Latest Version
    Set Log Level	TRACE
    Log To Console And Logfile      \nRemove All SPP and Upload Latest SPP
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}
    Wait For ALL Server Profile In Normal State
    Power off ALL servers   PressAndHold
    Remove All Firmware Bundles
    Setup Env For TBird    ${Ring}  ${Add_LE}  ${Add_Storage}  ${Team_Name}
    Log into Fusion appliance as Administrator
    ${rc} =     Fusion UI Add Latest Firmware Bundle    @{TestData.spps}
    Should Be True    ${rc}   msg=Failed to upload latest firmware bundles
    ${rc} =     Fusion Ui Logical Enclosure Firmware Update    @{TestData.editLE}
    Should Be True    ${rc}   msg=Failed to update LE firmware

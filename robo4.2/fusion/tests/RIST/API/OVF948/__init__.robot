*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keyword.txt
Variables   ./Regression_Data.py
Resource    ../../UI/resource.txt

#Suite Setup  Precondition Setup
Suite Teardown  Clear Profile And Firmware Bundle

*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                false
${UIDataFile}                   OVF948/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Keywords ***
Precondition Setup

    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}

	Remove All Server Profiles
	Remove All Firmware Bundles

	Load Test Data  ${UIDataFile}
    Log Variables
    Open Browser  ${ApplianceUrl}  ${Browser}
    Maximize Browser Window
    Run Keyword If  "${Browser}" == "ie"   Go To  javascript:document.getElementById('overridelink').click()
    Set Selenium Speed  ${SeleniumSpeed}
    Log into Fusion appliance as Administrator
    Fusion UI Add Firmware Bundle    @{TestData.spps}
    Close All Browsers

Clear Profile And Firmware Bundle
    Clear Test Environtment
    Remove All Firmware Bundles
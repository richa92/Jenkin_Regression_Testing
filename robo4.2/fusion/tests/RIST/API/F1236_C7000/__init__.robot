*** Settings ***
Resource    ../Fusion_Env_Setup/keywords.txt
Resource    ./keywords.txt
Variables   ./Regression_Data.py
Resource    ../../UI/resource.txt

Suite Setup  Precondition Setup         ${Firmware_Bundles}
Suite Teardown  Clear Profile And Firmware Bundle


*** Variables ***
${APPLIANCE_IP}                 ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}                    SHQA
${Ring}                         WPST32
${FTS}                          false
${Add_Storage}                  false
${Add_Enclosure}                true
${UIDataFile}                   F1236_C7000/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url


*** Keywords ***
Precondition Setup
    [Arguments]	            ${Firmware_Bundles}=${None}
    Set Log Level           TRACE
    ${resp}  ${sessionID}=  Fusion Api Login Appliance
    ...                     ${APPLIANCE_IP}         ${admin_credentials}
	Setup Env For C7000     ${Ring}     ${FTS}      ${Add_Enclosure}        ${Add_Storage}

	Run Keyword And Ignore Error    Wait For ALL Server Profile In Normal State
	Run Keyword And Ignore Error    Wait For ALL Servers Complete Refresh
    Run Keyword And Ignore Error    Power off ALL servers   PressAndHold
	Run Keyword And Ignore Error    Remove All Server Profiles
	Run Keyword And Ignore Error    Remove All Firmware Bundles

	Load Test Data  ${UIDataFile}
    Log Variables
    Open Browser  ${ApplianceUrl}  ${Browser}
    Maximize Browser Window
    Run Keyword If  "${Browser}" == "ie"   Go To  javascript:document.getElementById('overridelink').click()
    Set Selenium Speed  ${SeleniumSpeed}
    Log into Fusion appliance as Administrator
    Fusion UI Add Firmware Bundle    @{TestData.spps}
    Close All Browsers

#    Pass Execution If       ${Firmware_Bundles}==${None}        Skipped adding firmware bundle as Firmware_Bundles == None
#    ${status}=              Set Variable            ${False}
#    Run Keyword If          ${Firmware_Bundles}!=${None}
#    ...                     Fusion CLI Add Firmware Bundle
#    ...                     ${APPLIANCE_IP}
#    ...                     ${ssh_credentials}
#    ...                     ${sessionID}
#    ...                     ${Firmware_Bundles}
#	[Return]	${status}

Clear Profile And Firmware Bundle
    Clear Test Environtment
    Remove All Firmware Bundles
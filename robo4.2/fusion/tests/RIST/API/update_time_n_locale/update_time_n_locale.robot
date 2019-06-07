*** Settings ***
Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             OperatingSystem
Library             BuiltIn
Library             Collections
Library             json
Library             XML
Library             String
Library             Dialogs

Resource            ../../../../../fusion/Resources/api/fusion_api_resource.txt
Variables                       ${DATA_FILE}

*** Variables ***
${APPLIANCE_IP}     APPLIANCE_IP
${DATA_FILE}        ./Regression_data.py

*** Test Cases ***
Get Time and Locale
    Set Log Level   TRACE
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Get Appliance Time and Locale

Update Time and Locale
    ${resp} =    Configure Appliance Time and Locale    ${Time_and_Locale}
    Wait Until Keyword Succeeds    15 min    15 sec      OneView Startup Complete  ${APPLIANCE_IP}
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Wait For Task      ${resp}
    ${ntp_resp}     Get Appliance Time and Locale
    Verify NTP Servers      ${ntp_resp['ntpServers']}     ${Time_and_Locale['ntpServers']}



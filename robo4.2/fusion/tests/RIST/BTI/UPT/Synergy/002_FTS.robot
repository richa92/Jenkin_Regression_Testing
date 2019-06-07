*** Settings ***
Documentation       First Time Setup
Resource            resource.txt

*** Test Cases ***
Synergy UPT FTS First Time Setup
    [Documentation]     Configure First time setup for OneView Appliance
    First Time Setup  password=${admin_credentials['password']}
    Wait For Appliance To Become Pingable  ${APPLIANCE_IP}

Synergy UPT FTS Update Time and Locale
    [Documentation]     Configure Time and Locale for OneView Appliance
    ${resp} =    Configure Appliance Time and Locale    ${Time_and_Locale}
    Wait Until Keyword Succeeds    15 min    15 sec      OneView Startup Complete  ${APPLIANCE_IP}
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}
    Wait For Task      ${resp}
    ${ntp_resp}     Get Appliance Time and Locale
    Verify NTP Servers      ${ntp_resp['ntpServers']}     ${Time_and_Locale['ntpServers']}


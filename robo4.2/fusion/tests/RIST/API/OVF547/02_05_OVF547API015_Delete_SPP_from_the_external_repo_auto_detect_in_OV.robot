*** Settings ***
Documentation        Delete SPP from the external repo auto detect in OV
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables            ./Regression_Data.py

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF547/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Delete SPP from the external repo auto detect in OV
    Log    \n Starting Delete SPP from the external    console=true
    Run Multi Cmd   ${SERVER_IP}    ${ssh_username}    ${ssh_password}    ${remove_hotfix_commands}
    Wait Until Keyword Succeeds    120s    5s    Verify Firmware Status    ${detect_version}    ${bad_status}
    ${uri} =    Get Firmware Bundle By Version    ${detect_version}
    ${resp} =    Remove Firmware Bundle    ${uri}
    Wait For Task2    ${resp}    50    5
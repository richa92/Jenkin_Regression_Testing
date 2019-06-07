*** Settings ***
Documentation    Add An http external repository to Oneview using validate user credentials

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
Add An https external repository to Oneview using validate user credentials
    [Documentation]    Add An https external repository to Oneview using validate user credentials
    Log    \n Starting add web server as external repo    console=true
    Run Keyword And Ignore Error    Remove All Repositories
	Run Keyword And Ignore Error    Remove All Firmware Bundles
    Run Multi Cmd   ${SERVER_IP}    ${ssh_username}    ${ssh_password}    ${https_pw_commands}
    ${body} =   Generate HTTPS Request Payload    ${SERVER_IP}    ${Https_repo_with_password}
    ${resp} =    Add Repository       ${body}
    ${task} =   Wait For Task2       ${resp}     50    5
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Verify Firmwares Status   ${FirmwareVersions}    ${ok_status}
    Verify Firmwares Location   ${FirmwareVersions}    ${Expected_locations}    ${Unexpected_locations}
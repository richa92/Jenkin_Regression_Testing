*** Settings ***
Documentation    Add external repo with a SPP in internal repo

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
Add external repo with a SPP in internal repo
    [Documentation]    Add external repo with a SPP in internal repo

    Log    \n Starting add web server as external repo    console=true
    Upload Firmware Bundle Async    ${hpsut_path}
    ${uri} =    Get Firmware Bundle By Version    ${hpsut_version}
    Run Multi Cmd   ${SERVER_IP}    ${ssh_username}    ${ssh_password}    ${http_pw_commands}
    ${resp} =   Add Repository       ${Http_repo_with_password}
    ${task} =   Wait For Task2           ${resp}     50    5
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Verify Firmwares Status   ${FirmwareVersions}    ${ok_status}
    ${hpsut_versions} =    Create List    ${hpsut_version}
    Wait Until Keyword Succeeds    200s   5s    Verify Firmwares Location   ${hpsut_versions}    ${both_locations}    None

*** Settings ***
Documentation        Delete an SPP or hotfix which is present only in an internal repo from OneView will work
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
Delete an SPP or hotfix which is present only in an internal repo from OneView will work
    Log    \n Starting add web server as external repo    console=true
    Upload Firmware Bundle Async    ${ams_path}
    ${uri} =    Get Firmware Bundle By Version    ${ams_version}
    ${ams_versions} =    Create List    ${ams_version}
    Verify Firmwares Status   ${ams_versions}    ${ok_status}
    Verify Firmwares Location   ${ams_versions}    ${internal_locations}    ${external_locations}
    ${resp} =   Remove Firmware Bundle    ${uri}
    ${task} =   Wait For Task2           ${resp}     200    5
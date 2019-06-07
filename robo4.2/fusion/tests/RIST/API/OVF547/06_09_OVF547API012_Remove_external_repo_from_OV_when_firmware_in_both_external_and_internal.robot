*** Settings ***
Documentation        Remove external repo from OV when firmware in both external and internal
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
Remove external repo from OV when firmware in both external and internal
    Log    \n Starting delete external repo    console=true
    ${resp} =   Remove Repository By Name     ${repository_name}
    ${task} =   Wait For Task2           ${resp}     50    5
    ${uri} =    Get Firmware Bundle By Version    ${hpsut_version}
    ${hpsut_versions} =    Create List    ${hpsut_version}
    Wait Until Keyword Succeeds    50s   5s    Verify Firmwares Location   ${hpsut_versions}    ${internal_locations}    ${external_locations}
    Remove Firmware Bundle    ${uri}
*** Settings ***
Documentation        Refresh external repo and auto-discover the resources
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
Refresh external repo and auto-discover the resources
    Log    \n Starting Refresh external repo    console=true
    ${resp} =   Refresh Repository By Name       ${repository_name}
    ${task} =   Wait For Task2           ${resp}     50    5
    Wait Until Keyword Succeeds    200s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Verify Firmwares Status   ${FirmwareVersions}    ${ok_status}
    Verify Firmwares Location   ${FirmwareVersions}    ${Expected_locations}    ${Unexpected_locations}
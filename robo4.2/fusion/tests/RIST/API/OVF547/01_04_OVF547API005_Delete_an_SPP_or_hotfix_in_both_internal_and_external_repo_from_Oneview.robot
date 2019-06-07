*** Settings ***
Documentation        Delete an SPP or hotfix in both internal and external repo from Oneview
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
Delete an SPP or hotfix in both internal and external repo from Oneview
    Upload Firmware Bundle Async    ${hpsut_path}
    ${uri} =    Get Firmware Bundle By Version    ${hpsut_version}
    ${resp} =    Remove Firmware Bundle    ${uri}
    Wait For Task2    ${resp}    50    5
    ${hpsut_versions} =    Create List    ${hpsut_version}
    Verify Firmwares Location   ${hpsut_versions}    ${Expected_locations}    ${Unexpected_locations}
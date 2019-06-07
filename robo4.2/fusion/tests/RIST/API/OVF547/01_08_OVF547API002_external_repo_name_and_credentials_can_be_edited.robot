*** Settings ***
Documentation        External repo name and credentials can be edited
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
External repo name and credentials can be edited
    Log    \n Starting Edit external repo    console=true
    ${edit_body} =    Collections.Copy Dictionary     ${Http_repo_with_password}
    Remove From Dictionary    ${edit_body}    repositoryURI
    ${resp} =   Edit Repository       ${edit_body}    ${edit_repo}
    ${task} =   Wait For Task         ${resp}     50    5
    Wait Until Keyword Succeeds    200s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Verify Firmwares Status   ${FirmwareVersions}    ${ok_status}
    Verify Firmwares Location   ${FirmwareVersions}    ${expected_edit_locations}    ${Unexpected_locations}
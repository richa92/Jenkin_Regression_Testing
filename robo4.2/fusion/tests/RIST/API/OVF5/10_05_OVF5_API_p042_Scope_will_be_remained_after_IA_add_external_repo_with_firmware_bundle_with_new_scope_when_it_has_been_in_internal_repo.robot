*** Settings ***
Documentation    OVF5 Firmware SBAC test
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keyword.txt
Variables            ./Regression_Data.py

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF5/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
Scope will be remained after IA add external repo with firmware bundle with new scope when it has been in internal repo
    Log    \n Scope will be remained after IA add external repo with firmware bundle with new scope when it has been in internal repo    console=true
    ${resp} =   Add Repository       ${Http_repo_with_password}
    ${task} =   Wait For Task2           ${resp}     50    5
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Status   ${ValidateFirmwares}    ${ok_status}

    ${firmware} =    Get Firmware Bundle By Version  ${SPPVersion}
    :FOR    ${scope_name}    IN    @{ia_part_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Validate Resource Assign To Scope    ${scope}    ${firmware}
    ${scope} =    Get Scope URI By Name    ${ia_minor_scope}
    Validate Resource Not Assign To Scope    ${scope}    ${firmware}

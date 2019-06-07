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

Test Setup      Fusion Api Login Appliance         ${APPLIANCE_IP}        ${admin_credentials}

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF5/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url
${X-API-VERSION}    600

*** Test Cases ***
Firmware bundle scope should remained after appliance restart
    Log    \n Firmware bundle scope should remained after appliance restart    console=true
    ${spp} =    Get Firmware Bundle By Version  ${SPPVersion}
    ${hotfix} =    Get Firmware Bundle By Version  ${HotFixVersion}
    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_part_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${resp} =    Edit Resource Scope    ${spp}    ${scopes}
    Wait For Task2    ${resp}
    ${resp} =    Edit Resource Scope    ${hotfix}    ${scopes}
    Wait For Task2    ${resp}

    Restart Appliance
    Sleep    60
    Wait Until Keyword Succeeds    1800    10    OneView Startup Complete    ${APPLIANCE_IP}

    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}
    Wait Until Keyword Succeeds    800s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Wait Until Keyword Succeeds    800s   5s    Verify Firmwares Status   ${ValidateFirmwares}    ${ok_status}

    ${firmware} =    Get Firmware Bundle By Version  ${SPPVersion}
    :FOR    ${scope_name}    IN    @{ia_part_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Validate Resource Assign To Scope    ${scope}    ${firmware}
    ${scope} =    Get Scope URI By Name    ${ia_minor_scope}
    Validate Resource Not Assign To Scope    ${scope}    ${firmware}

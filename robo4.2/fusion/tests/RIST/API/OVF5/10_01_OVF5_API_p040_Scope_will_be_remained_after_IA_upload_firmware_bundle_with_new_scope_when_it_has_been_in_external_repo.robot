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

*** Test Cases ***
Scope will be overrided after IA upload firmware bundle with new scope when it has been in external repo
    Log    \n Scope will be overrided after IA upload firmware bundle with new scope when it has been in external repo    console=true
    Remove All Repositories
    ${resp} =    Remove All Firmware Bundles
    Wait For Task2    ${resp}
    ${resp} =   Add Repository       ${Http_repo_with_password}
    ${task} =   Wait For Task2           ${resp}     50    5
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Exist    ${ValidateFirmwares}
    Wait Until Keyword Succeeds    600s   5s    Verify Firmwares Status   ${ValidateFirmwares}    ${ok_status}

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

    Fusion Api Logout Appliance
    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${ia_credentials}

    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_user_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${scopes}=  Catenate List    ${scopes}

    Log    Uploading firmware bundle ${Upload_Exist_SPP_Path} with ${scopes}    console=true
    Upload Firmware Bundle With Scopes Async    ${Upload_Exist_SPP_Path}    ${scopes}
    ${firmware} =    Get Firmware Bundle By Version  ${SPPVersion}
    :FOR    ${scope_name}    IN    @{ia_part_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Validate Resource Assign To Scope    ${scope}    ${firmware}
    ${scope} =    Get Scope URI By Name    ${ia_minor_scope}
    Validate Resource Not Assign To Scope    ${scope}    ${firmware}

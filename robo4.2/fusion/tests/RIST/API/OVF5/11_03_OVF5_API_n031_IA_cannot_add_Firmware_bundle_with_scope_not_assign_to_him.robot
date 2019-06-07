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
IA cannot add Firmware bundle with scope not assign to him
    Log    \n IA cannot add Firmware bundle with scope not assign to him    console=true
    ${scopes} =  Create List
    :FOR    ${scope_name}    IN    @{ia_except_scopes}
    \    ${scope} =    Get Scope URI By Name    ${scope_name}
    \    Append To List    ${scopes}    ${scope}
    ${scopes}=  Catenate List    ${scopes}

    Log    Uploading firmware bundle ${Upload_SPP_Path} with ${scopes}    console=true
    ${resp} =    Upload Firmware Bundle With Scopes    ${Upload_SPP_Path}    ${scopes}
    Wait For Task2    ${resp}    600    10    PASS=Error    errorMessage=${creation_not_authorized_error}    VERBOSE=True

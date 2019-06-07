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
Firmware bundle should not added with unexisted scoped
    Log    \n Firmware bundle should not added with unexisted scoped    console=true

    Log    Uploading firmware bundle ${Upload_SPP_Path} with ${invalidScope}    console=true
    ${resp} =    Upload Firmware Bundle With Scopes    ${Upload_SPP_Path}    ${invalidScope}
    Wait For Task2    ${resp}    600    10    PASS=Error    errorMessage=${creation_not_authorized_error}    VERBOSE=True

*** Settings ***
Documentation        create custom SPP using remote base SPP and hotfixes
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
Test Setup      Run Keyword And Ignore Error     Remove Repository

*** Variables ***
${SELENIUM_TIMEOUT}         5.0
${SELENIUM_IMPLICIT_WAIT}   0.00
${DataFile}         OVF547/Regression_data.xml  # Data File Location
${ApplianceUrl}     https://${APPLIANCE_IP}     # Appliance Url

*** Test Cases ***
create custom SPP using remote base SPP and hotfixes
    Log    \n Starting create custom SPP    console=true
    ${baseline_uri} =    Get Firmware Bundle By Version  ${FirmwareVersion}
    ${hotfix_uri} =    Get Firmware Bundle By Version  ${smartarray_version}
    ${hotfixs} =    Create List    ${hotfix_uri}
    ${body} =    Create Dictionary    baselineUri=${baseline_uri}
	...								  customBaselineName=${custom_spp}
	...								  hotfixUris=${hotfixs}
	Log    Create custom SPP ${body}    console=true
    ${resp} =   Fusion Api Create Firmware Bundle     ${body}
    ${task} =   Wait For Task2           ${resp}     1000    20
    ${resp} =   Remove Repository By Name     ${repository_name}
    ${task} =   Wait For Task2           ${resp}     50    5
    ${uri} =    Get Firmware Bundle URI    ${custom_spp}
    ${resp} =   Remove Firmware Bundle    ${uri}
    ${task} =   Wait For Task2           ${resp}     50    5
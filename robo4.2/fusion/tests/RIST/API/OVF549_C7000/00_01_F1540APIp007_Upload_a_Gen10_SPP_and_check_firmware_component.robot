*** Settings ***
Documentation        Upload a Gen10 SPP and check firmware component
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
${APPLIANCE_IP}                 ${None}

*** Test Cases ***
Upload a Gen10 SPP and check firmware component
    Log    \n Starting validate firmware bundle    console=true
    ${uri} =    Get Firmware Bundle By Version  ${FirmwareVersion}
    ${spp} =    Get Firmware Bundle   ${uri}
    ${ComponentNames} =  Create List
    :FOR    ${Component}   IN  @{spp['fwComponents']}
	\   Append To List  ${ComponentNames}    ${Component['name']}
	:FOR    ${FirmwareName}   IN  @{ValidateFirmwares}
	\   Should Contain  ${ComponentNames}   ${FirmwareName}

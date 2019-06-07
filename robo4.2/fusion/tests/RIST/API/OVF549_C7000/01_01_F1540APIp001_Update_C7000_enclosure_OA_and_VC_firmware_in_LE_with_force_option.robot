*** Settings ***
Documentation        Update C7000 enclosure OA and VC firmware in LE with force option(Firmware should be updated)
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
Test Teardown   Remove All Enclosures
*** Variables ***
${APPLIANCE_IP}                 ${None}

*** Test Cases ***
Update C7000 enclosure OA and VC firmware in LE with force option(Firmware should be updated)
    Log    \n Starting update LE firmware    console=true
    Update Logical Enclosure Firmware       ${le_name}  ${FirmwareVersion}
    ${enc_firmware} =    Get Enclosure Firmware Version      ${enc_name}
    Should Be Equal    ${enc_firmware}    ${enc_fw}
    ${icm_firmware} =    Get Interconnect Firmware Version      ${icm_name}
    Should Be Equal    ${icm_firmware}    ${icm_fw}


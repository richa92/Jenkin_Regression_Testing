*** Settings ***
Documentation                   F607 server Firmware Update By LE
...                               -  F607 server Firmware Update By LE
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Setup           Get Run Specific Data File Variables Login the Users

*** Test Cases ***
F607APIp001 Update server firmware by creating LE with single enclosure
    Log to console and logfile    \n Starting creating LE firmware with firmware
    Create LE and update firmware    ${LE_NAME}  ${EG_Name}   ${LE_create_update_fw_force}
    Log to console and logfile    \n Starting validate server hardware firmware
    Validate server hardwares Firmware Version   ${server_hardwares}   ${Snap6SPP}


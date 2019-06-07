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
F607APIp004 update all servers by LE bigbang SharedInfrastructureAdnProfiles parallel force

    Log to console and logfile    \n Starting update LE firmware
    Update LE Firmware       ${LE_fw_update_SharedProfile_parallel_force}  ${LE_NAME}
    Log to console and logfile    \n Starting validate server hardware firmware
    Validate server hardwares Firmware Version   ${server_hardwares}   ${Snap6SPP}


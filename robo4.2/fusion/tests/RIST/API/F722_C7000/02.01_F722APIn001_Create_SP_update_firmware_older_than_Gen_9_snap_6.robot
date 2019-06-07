*** Settings ***
Documentation                   F722 Firmware Update By HPSUT offline
...                               -  Firmware Update By HPSUT offline
Library              FusionLibrary
Library              BuiltIn
Library              Collections
Library              json
Library              Dialogs
Library              String
Resource             ./../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt
Variables            ./Regression_Data.py
Test Setup           Get Run Specific Data File Variables Login the Users And Validate Firmware Bundle

*** Variables ***
# add your DCS appliance IP
${APPLIANCE_IP}        'DCS APPLIANCE IP'
${TARGET}            'C7000'
#C7000 or TBird
${DATA_FILE}         dcs_variables.py
*** Test Cases ***
F722APIn001 Create SP, update firmware older than Gen 9 snap 6
    [Tags]    Performance    server profiles-condition-gen9_firmware
    Update server firmware when create profile  ${SNAP5SPP}     ${True}    ${IP}
    :FOR    ${profile}    IN    @{createProfiles}
    \    ${sh} =    Get Server Hardware URI  ${profile['serverHardwareUri']}
    \    Fusion Api Refresh Server Hardware    uri=${sh}
    Wait For ALL Servers Complete Refresh
    Validate Profile Firmware Version   ${createProfiles}   ${SNAP5SPP}

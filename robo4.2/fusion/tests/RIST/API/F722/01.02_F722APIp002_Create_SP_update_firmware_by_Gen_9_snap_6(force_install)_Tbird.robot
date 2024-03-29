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
F722APIp002 Create SP, update firmware by Gen 9 snap 6 with force install
    [Tags]    Performance    server profiles-condition-gen9_firmware
    Update server firmware when create profile  ${SNAP6SPP}     ${True}
    Validate Profile Firmware Version   ${createProfiles}   ${SNAP6SPP}

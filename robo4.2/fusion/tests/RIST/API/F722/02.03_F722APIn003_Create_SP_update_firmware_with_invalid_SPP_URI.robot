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
F722APIn003 Create SP, update firmware with invalid SPP URI
    Clear Test Environtment
    ${profilelist} =    Generate profile body   ${createProfiles}   ${InvalidSPP}
    ${resps} =   Add Server Profiles from variable   ${profilelist}
    Validate Firmware Baseline Invalid Task     ${resps}
*** Settings ***
Documentation                   F1184 Local Storage Configuration By HPSUT
...                               -  Local Storage Configuration By HPSUT
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
F1184APIn004 Edit SP, update LocalStorage with invalid parameter
    Clear Test Environtment
    Create empty server profile  ${editProfiles}
    Log to console and logfile  Configure local storage, with invalid raid level
    ${profilelist} =    Generate Invalid Profile Body   ${editProfiles}
    ${resps} =   Edit Server Profiles from variable   ${profilelist}
    Validate Raid Level Invalid Task   ${resps}

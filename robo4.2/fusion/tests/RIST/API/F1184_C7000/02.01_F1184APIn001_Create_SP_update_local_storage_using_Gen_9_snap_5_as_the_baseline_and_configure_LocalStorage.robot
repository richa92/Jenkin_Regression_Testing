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
F1184APIn001 Create SP, update local storage using Gen 9 snap 3/4/5 as the baseline and configure LocalStorage
    Clear Test Environtment
    Log to console and logfile  Create SP, update local storage using Gen 9 snap5 as the baseline and configure LocalStorage
    ${profilelist} =    Generate Profile Body   ${createProfiles}   ${True}   ${SNAP5SPP}
    ${resps} =   Add Server Profiles from variable   ${profilelist}
    Validate Server Profile Task   ${resps}    ${IP}

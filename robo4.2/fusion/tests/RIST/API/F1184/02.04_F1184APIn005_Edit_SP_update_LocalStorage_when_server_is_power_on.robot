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
F1184APIn005 Edit SP, update LocalStorage when server is power on
    Clear Test Environtment
    Create empty server profile  ${editProfiles}
    Log to console and logfile  Power on servers
    ${body} =     Create Dictionary    powerState=On
    ...                                powerControl=MomentaryPress
    :FOR    ${profile}    IN    @{editProfiles}
    \    ${hardware} =   Get from Dictionary    ${profile}    serverHardwareUri
    \    ${sh_uri} =     Get Server Hardware URI        ${hardware}
    \    ${resp} =     Fusion Api Edit Server Hardware Power State        body=${body}    uri=${sh_uri}
    \    ${task} =    Wait For Task     ${resp}     240s    3s
    Log to console and logfile  Edit server profiles
    ${profilelist} =    Generate Profile Body   ${editProfiles}
    ${resps} =   Edit Server Profiles from variable   ${profilelist}
    :FOR    ${resp}    IN    @{resps}
    \    ${task} =    Wait For Task     ${resp}     10s    2s
    \    ${taskStatus} =    Get From Dictionary        ${task}     taskStatus
    \    ${taskState} =    Get From Dictionary        ${task}     taskState
    \    Log to console and logfile  ${taskStatus}
    \    Log to console and logfile  ${taskState}
    \    ${errorCode} =    Get From Dictionary        ${task['taskErrors'][0]}   errorCode
    \    Should Match    ${errorCode}    ServerNotOffProfileEdit

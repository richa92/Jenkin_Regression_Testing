*** Settings ***
Documentation        Verify unsupportive SHT can not Be imported using correct VC migration payload

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections

Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Resource             ../Fusion_Env_Setup/keywords.txt

Variables            ./Regression_Data.py

Test Setup           Setup Env For C7000  ${Ring}  ${FTS}  ${Add_Enclosure}  ${Add_Storage}  ${Team_Name}


*** Variables ***
${Enclosure}             WPST23
${APPLIANCE_IP}          ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}             SHQA
${Ring}                  ${Enclosure}
${FTS}                   false
${Add_Storage}           false
${Add_Enclosure}         true

*** Test Cases ***
Verify Unsupportive SHT Can Not Be Imported Using Correct VC Migration Payload
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Cleaning base Resources    console=true
    Clear Base Resources

    Log    Getting request body and parsing data file to get credentials...    console=true
    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}

    Log    Initializing the VCM configuration...    console=true
    ${backupFile}=                Get From Dictionary    ${vc_backup_file}    ${Enclosure}
    ${vc_config_file}=            Join Path    ${CURDIR}  \  ${backupFile}
    Delete and Re-configure VC Domain    ${vc_credentials['${Enclosure}']}  ${oa_credentials['${Enclosure}']}  ${vc_config_file}

    Log    Generating Compatibility Report...    console=true
    ${resourceUri}=               Create Migration Compatibility Report   ${requestBody}

    Log    Getting Compatibility Report...    console=true
    ${resp}  ${respState}=        Get Migration Compatibility Report      saveConfig=${False}

    Log    Migrating Enclosure from VC to OneView...    console=true
    Set TO Dictionary             ${migrationBody}    uri=${resourceUri}
    ${messages}=                  Get From Dictionary    ${resp}    items
    ${taskStatus}=                Run Keyword If    "${respState}" != "ReadyToMigrate"
    ...                           Fail    msg= The report state is not ReadyToMigrate, please manually fix error.\n${messages}.
    ...                           ELSE    Add Enclosure By Migration  ${resourceUri}  ${migrationBody}
    should Not Be Equal           '${taskStatus}'    'Error'    msg=Migration task status should be "Completed/Warning"

    Log    Verifying Server Hardware Types same as expect...    console=true
    ${expectSHTs}=                Get From Dictionary  ${expect_sever_hardware_types}  ${Enclosure}
    ${shts}=                      Fusion Api Get Server Hardware Types
    Length Should Be              ${shts['members']}  5
    :FOR                          ${sht}    IN    @{shts['members']}
    \                             Validate Response Regex    ${sht}    ${expectSHTs}

    Log    Verifing Server Profiles same as expect...    console=true
    ${expectSPs}=                 Get From Dictionary  ${expect_sever_profiles}  ${Enclosure}
    ${sps}=                       Fusion Api Get Server Profiles
    Length Should Be              ${sps['members']}  5
    :FOR                          ${sp}    IN    @{sps['members']}
    \                             Validate Response Regex    ${sp}    ${expectSPs}

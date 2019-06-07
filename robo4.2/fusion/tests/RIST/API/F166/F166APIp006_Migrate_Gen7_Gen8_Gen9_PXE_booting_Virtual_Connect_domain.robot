*** Settings ***
Documentation        Migrate Gen7 gen8 gen9 to Virtual Connect domain

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections

Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Variables            ./Regression_Data.py

Test Teardown        Pause And Clear Base Resources    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}      unknown
${Enclosure}         WPST26
${net}               Network_300

*** Test Cases ***
Migrate Gen7 gen8 gen9 to Virtual Connect domain
    Log    \nLogging in OneView appliance    console=True
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Getting request body and parsing data file to get credentials...    console=True
    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}

    Log    Initializing the VCM configuration...    console=True
    ${backupFile}=                Get From Dictionary    ${vc_backup_file}    ${Enclosure}
    ${vc_config_file}=            Join Path    ${CURDIR}  \  ${backupFile}
    Delete and Re-configure VC Domain    ${vc_credentials['${Enclosure}']}  ${oa_credentials['${Enclosure}']}  ${vc_config_file}

    Log     Waiting blade server booting to OS...
    :FOR    ${ilo}  IN    @{ilo_list}
    \       Wait for Blade to reach POST State Using ILO  ${ilo}

    Log    Generating Compatibility Report...    console=True
    ${resourceUri}=               Create Migration Compatibility Report   ${requestBody}

    Log    Getting Compatibility Report...    console=True
    ${resp}  ${respState}=        Get Migration Compatibility Report      saveConfig=${False}

    Log    Migrating Enclosure from VC to OneView...    console=True
    Set TO Dictionary             ${migrationBody}    uri=${resourceUri}
    ${messages}=                  Get From Dictionary    ${resp}    items
    ${taskStatus}=                Run Keyword If    "${respState}" != "ReadyToMigrate"
    ...                           Fail    msg= The report state is not ReadyToMigrate, please manually fix error.\n${messages}.
    ...                           ELSE    Add Enclosure By Migration  ${resourceUri}  ${migrationBody}
    should Not Be Equal               '${taskStatus}'    'Error'    msg=Migration task status should not be "Error"

    Log    Verifying Server Hardware same as expect...    console=True
    ${expectSHs}=                Get From Dictionary  ${expect_sever_hardware}  ${Enclosure}
    ${shkeys} =      Get From Dictionary    ${expectSHs}   name
    :FOR              ${sh}    IN    @{shkeys}
    \                 Run Keyword If    '${sh}' == 'wpst26, bay 1' or '${sh}' == 'wpst26, bay 9' or '${sh}' == 'wpst26, bay 7' or '${sh}' == 'wpst26, bay 4'  Verify Server Profiles Non Assigned     ${sh}
    \  ...            ELSE      Vefiry Server Profiles Assigned     ${sh}


    Log    Verifing Server Profiles same as expect...    console=True
    ${expectSPs}=                 Get From Dictionary  ${expect_sever_profiles}  ${Enclosure}
    ${spkeys} =      Get From Dictionary    ${expectSPs}   name
    :FOR              ${sp}    IN    @{spkeys}
    \                 run keyword if  '${sp}' == '${PXE_bay8_profiles}' or '${sp}' == '${PXE_bay10_profiles}'   Verify Server Profiles Status And Boot    ${sp}  ${net}
    \  ...            ELSE    Verify Server Profiles Status  ${sp}

*** Settings ***
Documentation        Migrate Gen6 gen5 gen9 booting OS into Virtual Connect Domain

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
Test Teardown        Pause And Clear Base Resources    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}      ${None}         # leave it as ${None} if you want this test to create a new one
${Enclosure}         WPST22
${Team_Name}         SHQA
${Ring}              ${Enclosure}
${FTS}               false
${Add_Storage}       false
${Add_Enclosure}     true


*** Test Cases ***
Migrate Gen6 gen5 gen9 booting OS into Virtual Connect Domain
    ${ilo_list}=    Get All Server Hardwares iLO IP Except Gen5/Gen6
    Log    Logging in OneView appliance    console=True
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Cleaning base Resources    console=True
    Clear Base Resources

#    Log    Add enclosure as monitor    console=True
#    Clear Multi OA VC Mode  ${WPST22Encls}
#    Add Enclosures from variable      ${Monitored22}  25min

    Log    Getting request body and parsing data file to get credentials...    console=True
    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}

    Log    Initializing the VCM configuration...    console=True
    ${backupFile}=                Get From Dictionary    ${vc_backup_file}    ${Enclosure}
    ${vc_config_file}=            Join Path    ${CURDIR}  \  ${backupFile}
    Delete and Re-configure VC Domain    ${vc_credentials['${Enclosure}']}  ${oa_credentials['${Enclosure}']}  ${vc_config_file}

    Log To Console     Waiting blade server booting to OS...    console=True
    :FOR    ${ilo}  IN    @{ilo_list}
    \       Wait for Blade to reach POST State Using ILO  ${ilo}
    sleep  300

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
    should Not Be Equal               '${taskStatus}'    'Error'    msg=Migration task status should be "Completed"

    Log    Verifying Server Hardware same as expect...    console=True
    ${expectSHs}=                Get From Dictionary  ${expect_sever_hardware}  ${Enclosure}
    ${shkeys} =      Get From Dictionary    ${expectSHs}   name
    :FOR              ${sh}    IN    @{shkeys}
    \                 Run Keyword If    '${sh}' == 'wpst22, bay 6'      Verify Gen6 Server Hardware PowerState And State     ${sh}
    \  ...            ELSE IF   '${sh}' == 'wpst22, bay 8'     Verify Gen5 Server Hardware PowerState And State     ${sh}
    \  ...            ELSE      Verify Gen7 to Gen9 Server Hardware PowerState     ${sh}

    Log    Verifing Server Profiles same as expect...    console=True
    ${expectSPs}=                 Get From Dictionary   ${expect_sever_profiles}  ${Enclosure}
    ${spkeys} =      Get From Dictionary    ${expectSPs}   name
    :FOR                          ${sp}    IN    @{spkeys}
    \                             Verify Server Profiles Status     ${sp}

    Log    Logging out OneView appliance    console=True
    Fusion Api Logout Appliance

*** Settings ***
Documentation        Migrate enclosure with two vlan ethernet networks link to one external port


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
${Enclosure}         WPST26
${EnclosureCopy}     WPST261
${net}               Network_300
${Team_Name}         SHQA
${Ring}              ${Enclosure}
${FTS}               false
${Add_Storage}       false
${Add_Enclosure}     true

*** Test Cases ***
Migrate enclosure with two vlan ethernet networks link to one external port
    ${ilo_list}=    Get All Server Hardwares iLO IP Except Gen5/Gen6
    Set Global Variable  ${ilo_list}
    Log    Logging in OneView appliance    console=True
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Cleaning base Resources    console=True
    Clear Base Resources

    Log    Getting request body and parsing data file to get credentials...    console=True
    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}

    Log    Initializing the VCM configuration...    console=True
    ${backupFile}=                Get From Dictionary    ${vc_backup_file}    ${EnclosureCopy}
    ${vc_config_file}=            Join Path    ${CURDIR}  \  ${backupFile}
    Delete and Re-configure VC Domain    ${vc_credentials['${Enclosure}']}  ${oa_credentials['${Enclosure}']}  ${vc_config_file}

    Log     Waiting blade server booting to OS...    console=True
    :FOR    ${ilo}  IN    @{ilo_list}
    \       Wait for Blade to reach POST State Using ILO  ${ilo}

    Log     Add enclosure as monitor....    console=True
    Run Keyword And Ignore Error    Add Enclosures from variable      ${Monitored26}  25min
    Remove ALl Enclosures          param=?force=true

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
    \                 Run Keyword If    '${sh}' == 'wpst26, bay 1' or '${sh}' == 'wpst26, bay 9' or '${sh}' == 'wpst26, bay 7' or '${sh}' == 'wpst26, bay 4'   Verify Server Profiles Non Assigned     ${sh}
    \  ...            ELSE      Vefiry Server Profiles Assigned     ${sh}


    Log    Verifing Server Profiles same as expect...    console=True
    ${expectSPs}=                 Get From Dictionary  ${expect_sever_profiles}  ${Enclosure}
    ${spkeys} =      Get From Dictionary    ${expectSPs}   name
    :FOR              ${sp}    IN    @{spkeys}
    \                 run keyword if  '${sp}' == '${PXE_bay8_profiles}' or '${sp}' == '${PXE_bay10_profiles}'   Verify Server Profiles Status And Boot    ${sp}  ${net}
    \  ...            ELSE    Verify Server Profiles Status  ${sp}

    Log    Logging out OneView appliance    console=True
    Fusion Api Logout Appliance

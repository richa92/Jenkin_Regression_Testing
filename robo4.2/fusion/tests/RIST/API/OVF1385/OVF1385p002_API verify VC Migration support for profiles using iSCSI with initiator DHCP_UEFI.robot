*** Settings ***
Documentation        VC Migration support for profiles using iSCSI with initiator DHCP

Library              FusionLibrary
Library              RoboGalaxyLibrary
Library              OperatingSystem
Library              BuiltIn
Library              Collections

Resource             ../Fusion_Env_Setup/keywords.txt
Resource             ../../../../Resources/api/fusion_api_resource.txt
Resource             ./keywords.txt

Variables            ${DATA_FILE}

Test Teardown        Clear Base Resources    ${APPLIANCE_IP}    ${admin_credentials}

*** Variables ***
${APPLIANCE_IP}      ${None}         # leave it as ${None} if you want this test to create a new one
${Enclosure}         WPST23
${Team_Name}         SHQA
${Ring}              ${Enclosure}
${FTS}               false
${Add_Storage}       false
${Add_Enclosure}     true


*** Test Cases ***
OVF1385p002_API verify VC Migration support for profiles using iSCSI with initiator DHCP_UEFI
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'

    Clear Base Resources          ${APPLIANCE_IP}    ${admin_credentials}

    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}

    ${backupFile}=                Get From Dictionary    ${vc_backup_file_uefi}    ${Enclosure}
    ${vc_config_file}=            Join Path    ${CURDIR}  \  ${backupFile}
    Delete and Re-configure VC Domain    ${vc_credentials['${Enclosure}']}  ${oa_credentials['${Enclosure}']}  ${vc_config_file}

    ${resourceUri}=               Create Migration Compatibility Report   ${requestBody}

    ${resp}  ${respState}=        Get Migration Compatibility Report      saveConfig=${False}

    Set TO Dictionary             ${migrationBody}    uri=${resourceUri}
    ${messages}=                  Get From Dictionary    ${resp}    items
    ${taskStatus}=                Run Keyword If    "${respState}" != "ReadyToMigrate"
    ...                           Fail    msg= The report state is not ReadyToMigrate, please manually fix error.\n${messages}.
    ...                           ELSE    Add Enclosure By Migration  ${resourceUri}  ${migrationBody}
    should Not Be Equal           '${taskStatus}'    'Error'    msg=Migration task status should be "Completed"

    ${expectSPs}=                 Get From Dictionary    ${expect_sever_profiles}  ${Enclosure}
    ${spkeys} =                   Get From Dictionary    ${expectSPs}   name
    ${iscsi_exp} =                Get From Dictionary    ${expect_iscsi_info}   iscsi
    :FOR                          ${sp}    IN    @{spkeys}
    \                             Verify Server Profiles Status And Connections     ${sp}  ${iscsi_exp}

    Fusion Api Logout Appliance

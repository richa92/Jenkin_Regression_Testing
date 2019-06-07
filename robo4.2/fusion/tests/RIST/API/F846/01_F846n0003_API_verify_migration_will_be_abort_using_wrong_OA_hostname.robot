*** Settings ***
Documentation        Verify Migration Will Be Abort Using Wrong OA Hostname

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
${Enclosure}             WPST22
${APPLIANCE_IP}          ${None}         # leave it as ${None} if you want this test to create a new one
${Team_Name}             SHQA
${Ring}                  ${Enclosure}
${FTS}                   false
${Add_Storage}           false
${Add_Enclosure}         true

*** Test Cases ***
Verify Migration Will Be Abort Using Wrong OA Hostname
    Log    Logging in OneView appliance    console=true
    Should Not Be Equal           ${APPLIANCE_IP}  unknown  msg=The appliance IP must be defined, Example:'APPLIANCE_IP:16.114.220.131'
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

    Log    Cleaning base Resources    console=true
    Clear Base Resources

    Log    Getting request body and parsing data file to get credentials...    console=true
    ${requestBody}=               Get From Dictionary    ${all_hardware_info}    ${Enclosure}
    ${requestBody1}=              Wpst Deep Copy         ${requestBody}

    Log    Generating an error OA hostname for request body...    console=true
    ${expectHostname}=            Get From Dictionary    ${requestBody1["credentials"]}  oaIpAddress
    Set To Dictionary             ${requestBody1["credentials"]}  oaIpAddress=wpst_error-oa2.vse.rdlabs.hpecorp.net
    ${actualHostname}=            Get From Dictionary    ${requestBody1["credentials"]}  oaIpAddress
    Should Not Be Equal           ${expectHostname}  ${actualHostname}  msg=This case used to verify wrong hostname, please provide a wrong OA password

    Log    Initializing the VCM configuration...    console=true
    ${backupFile}=                Get From Dictionary    ${vc_backup_file}    ${Enclosure}
    ${vc_config_file}=            Join Path    ${CURDIR}  \  ${backupFile}
    Delete and Re-configure VC Domain    ${vc_credentials['${Enclosure}']}  ${oa_credentials['${Enclosure}']}  ${vc_config_file}

    Log    Generating Compatibility Report...    console=true
    ${resourceUri}=               Create Migration Compatibility Report   ${requestBody1}
    Should Be Equal               ${resourceUri}  ${None}  msg=The task should be failed

    Log    Verifying Server Hardware Types can not be imported    console=true
    ${SHTs}=                      Fusion Api Get Server Hardware Types
    Should Be Empty               ${SHTs["members"]}  msg=The server hardware types shoud not be created, please check.

    Log    Verifing Server Profiles same as expect...    console=true
    ${SPs}=                       Fusion Api Get Server Profiles
    Should Be Empty               ${SPs["members"]}  msg=The server profiles shoud not be created, please check.

    Log    Logging out OneView appliance    console=true
    Fusion Api Logout Appliance

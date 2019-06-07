*** Settings ***
Documentation                   Gen10 SYN Server profiles and templates for BIOS to test Dynamic BIOS Registry Feature

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             OperatingSystem
Library             SSHLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             XML
Library             String
Library             Dialogs
Library             OVS11171_BIOS_functions
Library             ./../../../../Resources/api/common/RisHelpers.py
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ./OVS11171_Regression_Data.py

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}        ${Syn_fusion_ip}


*** Test Cases ***
OVS11171-TC1 Delete registry Get Server Info Refresh Server and Check Bios family folder
    [TAGS]    Start
    Get Server Family Info from variable     ${Syn_test_server_list}
    Delete the latest registry files in OV
    Refresh SYN Gen10 server as managed      ${Syn_name}
    Check for BiosFamily Folder in OV

OVS11171-TC2 Confirm for the relevant file present in OV
    Check for latest registry file using variable     ${Syn_test_server_list}
    Read OV file to Dictionary using variable    ${Syn_test_server_list}

OVS11171-TC3 Compare Dictionary of Server and OV Files
    Compare Server and OV BiosReg Content using variable    ${Syn_test_server_list}
    Sht details to dictionary and list using variable    ${Syn_test_server_list}

OVS11171-TC4 Create SYN Gen10 SPT
    [TAGS]    Template
    Create SYN Gen10 Server Profile Template

OVS11171-TC5 Create SYN Gen10 Profiles using the SPT
    [TAGS]    Profile
    Create SYN Gen10 Server Profiles

OVS11171-TC6 Get Second Server Details and Refresh the server
    Get Server Family Info from variable    ${Syn_test_server_list_rom_upgraded}
    Refresh SYN Gen10 server as managed      ${Syn_name2}

OVS11171-TC7 Confirm for the latest file present in OV After Refreshing Second Server
    Check for latest registry file using variable     ${Syn_test_server_list_rom_upgraded}
    Read OV file to Dictionary using variable    ${Syn_test_server_list_rom_upgraded}

OVS11171-TC8 Compare Dictionary of Server and OV Files After Refreshing Second Server
    Compare Server and OV BiosReg Content using variable    ${Syn_test_server_list_rom_upgraded}
    Sht details to dictionary and list using variable    ${Syn_test_server_list_rom_upgraded}

OVS11171-TC9 Compare both SHT to know if they are matching
    Compare both SHT BIOS Details

OVS11171-TC10 Edit SYN Gen10 SP
    [TAGS]    ProfEdit
    Edit SYN Gen10 Server Profiles

OVS11171-TC11 Check Profile if NonCompliant with Template
    [TAGS]    Compliant
    Check Profile if NonCompliant with Template


*** Keywords ***
Setup
    [Documentation]    OVS11171 Gen10 Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${Syn_admin_credentials}

Clean Up
    [Documentation]    OVS11171 Gen10 Teardown
    ${resps} =    Remove Server Profiles from variable    ${Syn_gen10_server_profiles}
    Wait For Task2    ${resps}    timeout=15m    interval=5
    Remove Server Profile Templates from variable    ${Syn_gen10_profile_templates}
    Fusion Api Logout Appliance

Delete the latest registry files in OV
    [Documentation]    OVS11171 To Delete the existing registry files (which belong to the particular bios family) from OneView
    ${id}=        Open Connection     ${Syn_fusion_ip}
    ${output} =   Login    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    ${keys_Family}     Get Dictionary Keys     ${Syn_server_fam_and_reg_ver}
    :FOR     ${ELEMENT}     IN     @{keys_Family}
    \    ${stdOutput}=     Execute Command     ls /ci/data/registries/bios
    \    ${command}=     Convert to Lowercase     rm -rf /ci/data/registries/bios/${ELEMENT}
    \    ${match}     ${value}    Run Keyword And Ignore Error     Should Contain     ${stdOutput}     ${ELEMENT}     ignore_case=True
    \    ${RETURNVALUE}     Set Variable If     '${match}' == 'PASS'     ${True}     ${False}
    \    Run Keyword If     ${RETURNVALUE}     Execute Command     ${command}

Get Server Family Info from variable
    [Documentation]    OVS11171 Fetches the Server BIOS Information from iLO using the curl command in OV (this is
    ...                in consideration of - iLO not in the same network where the testscripts are running but the OV is available to the TestScript)
    [Arguments]     ${GivenServerList}
    ${id}=        Open Connection     ${Syn_fusion_ip}
    ${usr}    Get From Dictionary    ${Syn_ilo_credentials}    username
    ${pwd}    Get From Dictionary    ${Syn_ilo_credentials}    password
    ${output} =   Login    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    :FOR     ${ELEMENT}     IN     @{GivenServerList}
    \    ${iLOIpForCommand}    Get From Dictionary     ${ELEMENT}     iLOIp
    \    ${stdOutput} =    Execute Command    /usr/bin/curl -ik --user "${usr}:${pwd}" https://${iLOIpForCommand}/redfish/v1/systems/1/bios/
    \    Should Contain    ${stdOutput}    AttributeRegistry    ignore_case=True
    \    ${attribute_Reg}     ${cpu_Famiy}     ${version_Info} =     find registry details    ${stdOutput}
    \    Set to Dictionary     ${ELEMENT}     cpu_Famiy     ${cpu_Famiy}
    \    Set to Dictionary    ${ELEMENT}    version_Info     ${version_Info}
    \    Set to Dictionary    ${ELEMENT}    attribute_Reg    ${attribute_Reg}
    \    ${keys_Family}     Get Dictionary Keys     ${Syn_server_fam_and_reg_ver}
    \    Log    \n${keys_Family}
    \    ${familyExists} =     Get Index From List        ${keys_Family}     ${cpu_Famiy}
    \    Run Keyword If     ${familyExists} == 0     Check And Update Dictionary    ${Syn_server_fam_and_reg_ver}     ${cpu_Famiy}    ${attribute_Reg}
    \    Run Keyword If     ${familyExists} < 0        update to dictionary     ${Syn_server_fam_and_reg_ver}     ${cpu_Famiy}    ${attribute_Reg}
    \    Log    ${Syn_server_fam_and_reg_ver}
    \    ${stdOutput1} =    Execute Command    /usr/bin/curl -ik --compressed --user "${usr}:${pwd}" https://${iLOIpForCommand}/redfish/v1/registrystore/registries/en/${attribute_Reg}/
    \    ${fileContentFromServer}=    get json from raw data     ${stdOutput1}
    \    Set To Dictionary    ${ELEMENT}     ServerFileContent     ${fileContentFromServer}

Check And Update Dictionary
    [Documentation]    OVS11171 This acts as a supporting keyword for "Get Server Family Info from variable"
    ...                 This keyword is required as to check if the registry is already present or not and then perform the dictionary update accordingly.
    [Arguments]     ${Syn_server_fam_and_reg_ver}
    ...             ${cpu_Famiy}
    ...             ${attribute_Reg}
    ${key_Reg}     Get From Dictionary     ${Syn_server_fam_and_reg_ver}     ${cpu_Famiy}
    ${keyExists}     Get Index From List     ${key_Reg}     ${attribute_Reg}
    Run Keyword If     ${keyExists} < 0     Append To List     ${key_Reg}     ${attribute_Reg}
    Sort List     ${key_Reg}
    Set to Dictionary     ${Syn_server_fam_and_reg_ver}     ${cpu_Famiy}    ${key_Reg}

Refresh SYN Gen10 server as managed
    [Documentation]    Refresh server hardware.
    ...                    Refresh Server Hardware  SH:${ENC1SHBAY1}
    ...                    Refresh Server Hardware  ${ENC1SHBAY1}
    [Arguments]     ${name}
    ${payload} =     Create Dictionary    refreshState=RefreshPending
    ${name} =  replace string using regexp  ${name}  SH:  ${EMPTY}
    Log      \nRefreshing server ${name}    console=True
    ${server} =  Get Resource  SH:${name}
    ${resp} =     Fusion Api Refresh Server Hardware  body=${payload}  uri=${server['uri']}
    Wait For Task2    ${resp}    timeout=2400    interval=15
    [return]  ${resp}

Check for BiosFamily Folder in OV
    [Documentation]    OVS11171 Checks if the appropriate BIOS Family Folder exists in the OV.
    ${id}=     Open Connection        ${Syn_fusion_ip}
    ${output}=         Login    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    ${stdOutput}=     Execute Command     ls /ci/data/registries/bios
    ${keys_Family}     Get Dictionary Keys     ${Syn_server_fam_and_reg_ver}
    :FOR     ${ELEMENT}     IN     @{keys_Family}
    \    Should Contain    ${stdOutput}    ${ELEMENT}    ignore_case=True

Check for latest registry file using variable
    [Documentation]    OVS11171 Checks if the appropriate BIOS Family's latest file
    [Arguments]     ${GivenVariable}
    ${id}=     Open Connection        ${Syn_fusion_ip}
    ${output}=         Login    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    ${keys_Family}     Get Dictionary Keys     ${Syn_server_fam_and_reg_ver}
    :FOR     ${Key_ELEMENT}     IN     @{keys_Family}
    \    ${cpu_Famiy}=    Convert to Lowercase    ${Key_ELEMENT}
    \    ${stdOutput}=     Execute Command     ls /ci/data/registries/bios/${cpu_Famiy}/en
    \    @{Files_Available_in_OV} =     Split String     ${stdOutput}
    \    ${stdOutput1}=     Execute Command     ls /ci/data/registries/bios/${cpu_Famiy}/ja
    \    ${stdOutput2}=     Execute Command     ls /ci/data/registries/bios/${cpu_Famiy}/zh
    \    ${Values_Family}     Get From Dictionary     ${Syn_server_fam_and_reg_ver}     ${Key_ELEMENT}
    \    ${latest_RegVer} =     Get From List    ${Values_Family}     -1
    \    Should Contain     ${StdOutput}    ${latest_RegVer}
    \    Should Contain     ${StdOutput1}    ${latest_RegVer}
    \    Should Contain     ${StdOutput2}    ${latest_RegVer}
    \    Sort List     ${Files_Available_in_OV}
    \    ${latest_File_in_OV}=     Get From List     ${Files_Available_in_OV}     -1
    \    Loop over GivenServers    ${GivenVariable}    ${key_ELEMENT}         ${latest_File_in_OV}
    \    Should be Equal         ${latest_File_in_OV}     ${latest_RegVer}.json

Loop over GivenServers
    [Documentation]    OVS11171 This acts as a supporting keyword for "Check for latest registry file using variable"
    ...                 This keyword is required as the Loop inside a loop is not allowed.
    [Arguments]     ${Servers}
    ...                ${cpu_Famiy}
    ...                ${latest_File_in_OV}
    :FOR     ${ELEMENT}     IN     @{Servers}
    \    ${CpuFam}     Get From Dictionary     ${ELEMENT}      cpu_Famiy
    \    Run Keyword If     '${CpuFam}' == '${cpu_Famiy}'     Set To Dictionary     ${ELEMENT}     latest_File_in_OV     ${latest_File_in_OV}

Read OV file to Dictionary using variable
    [Documentation]    OVS11171 Reads the Registry Files from OV and Stores it into the dictionary for later verification
    [Arguments]     ${Servers}
    Login to Fusion via SSH
    Set Default Configuration    timeout=900    # Some commands (below) take a long time
    :FOR     ${Element}     IN     @{Servers}
    \    ${cpu_fam}=     Get From Dictionary     ${ELEMENT}     cpu_Famiy
    \    ${cpu_Famiy}=     Convert to Lowercase     ${cpu_fam}
    \    ${latest_file_in_ov}=     Get From Dictionary     ${ELEMENT}     latest_File_in_OV
    \    ${stdout}    ${stderr}    ${rc}=    Execute Command    cat /ci/data/registries/bios/${cpu_Famiy}/en/${latest_file_in_ov}    return_stderr=True    return_rc=True
    \    Should Be Empty    ${stderr}                 msg=Error returned: ${rc} ${stderr}
    \    Should Be Equal As Integers    ${rc}    0    msg=non-zero return code ${rc}
    \    Set To Dictionary    ${ELEMENT}     OvFileContent     ${stdout}
    Logout of Fusion Via SSH

Compare Server and OV BiosReg Content using variable
    [Documentation]    OVS11171 Get the Bios Details from Server and also Read the Bios Details from Registry File in OV and Compare them
    [Arguments]     ${Servers}
    :FOR     ${Element}     IN     @{Servers}
    \    ${ov_file}=     Get From Dictionary     ${ELEMENT}     OvFileContent
    \    ${server_file}=     Get From Dictionary     ${ELEMENT}     ServerFileContent
    &{dict1} =     string to dictionary     ${ov_file}
    &{dict2} =     string to dictionary     ${server_file}
    ${retval}=    compare dictionary    Syn        Basic        ${dict1}    ${dict2}
    Should Be True    ${retval}

Sht details to dictionary and list using variable
    [Documentation]    OVS11171 Get the SHT Details from Server and Stores it into the dictionary for the later verification
    [Arguments]        ${Servers}
    ${id}=        Open Connection     ${Syn_fusion_ip}
    ${output} =   Login    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    ${usr}=     Get From Dictionary     ${Syn_admin_credentials}     userName
    ${pwd}=     Get From Dictionary     ${Syn_admin_credentials}     password
    ${output}=    Execute Command     /usr/bin/curl -k -s -S -X POST -d '{"userName":"${usr}", "password":"${pwd}"}' -H "Content-Type: application/json" -H "Accept: application/json" "https://localhost/authn/rest/login-sessions" |cut -d'"' -f4
    :FOR     ${Element}     IN     @{Servers}
    \    ${svrname}=     Get From Dictionary     ${ELEMENT}     ServerName
    \    ${sht_uri}=    Get Server Hardware Type URI By Server Hardware     ${svrname}
    \    Set To Dictionary     ${ELEMENT}     ShtUri    ${sht_uri}
    \    ${stdOutput1} =    Execute Command    /usr/bin/curl -k -s -S -X GET -H "x-api-version: ${Syn_api_version}" -H "Content-Type: application/json" -H "Accept: application/json" -H "auth:${output}" "https://localhost${sht_uri}"
    \    &{dict} =     string to dictionary     ${stdOutput1}
    \    @{List}=     Get From Dictionary     ${dict}        biosSettings
    \    Set To Dictionary     ${ELEMENT}     ShtBiosSettings     ${List}
    \    Append To List     ${Syn_bios_details_from_sht}     {${List}}

Check Profile if NonCompliant with Template
    [Documentation]    OVS11171 After Creating and Editing the Server Profile and Templates, Checks if the Template and Profile are Non-Compliant.
    ${id}=     Open Connection     ${Syn_fusion_ip}
    ${output}=     Login    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    ${usr}=     Get From Dictionary     ${Syn_admin_credentials}     userName
    ${pwd}=     Get From Dictionary     ${Syn_admin_credentials}     password
    ${output}=    Execute Command     /usr/bin/curl -k -s -S -X POST -d '{"userName":"${usr}", "password":"${pwd}"}' -H "Content-Type: application/json" -H "Accept: application/json" "https://localhost/authn/rest/login-sessions" |cut -d'"' -f4
    &{prof_dict}=     Get From List     ${SYN_gen10_server_profiles}     0
    ${prof_name}=     Get From Dictionary     ${prof_dict}     name
    ${svr_prof_uri}=     Get Server Profile URI     ${prof_name}
    ${ProfDetails} =    Execute Command    /usr/bin/curl -k -s -S -X GET -H "x-api-version: ${Syn_api_version}" -H "Content-Type: application/json" -H "Accept: application/json" -H "auth:${output}" "https://localhost${svr_prof_uri}"
    &{prof_dict} =     string to dictionary     ${ProfDetails}
    ${temp_compliant}=    Get From Dictionary     ${prof_dict}    templateCompliance
    Should Not Be Equal     ${temp_compliant}     NonCompliant

Compare both SHT BIOS Details
    [Documentation]    OVS11171 Compares both the SHT BIOS Details of older and newer versions of the BIOS Registry files
    ${dict1} =     Get From List     ${Syn_bios_details_from_sht}    0
    ${dict2} =     Get From List     ${Syn_bios_details_from_sht}    1
    Log     \n${dict1}
    Log     \n${dict2}
    ${retval}=    compare dictionary    Syn    Full     ${dict1}    ${dict2}
    Should Not Be True     ${retval}

Create SYN Gen10 Server Profile Template
    [Documentation]  Create SYN Gen10 Server Profile Template
    Power off Servers in Profiles  ${Syn_gen10_server_profiles}
    @{responses} =    Create List
    :FOR    ${profile_template}    IN    @{Syn_gen10_profile_templates}
    \      ${resp} =     Add Server Profile Template    ${profile_template}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}       timeout=60    interval=5

Create SYN Gen10 Server Profiles
    [Documentation]  Create SYN Gen10 Server Profiles
    Power off Servers in Profiles  ${Syn_gen10_server_profiles}
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{Syn_gen10_server_profiles}
    \      ${resp} =     Add Server Profile    ${server_profile}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2400    interval=15

Edit SYN Gen10 Server Profiles
    [Documentation]  Edit SYN Gen10 Server Profiles
    @{responses} =    Create List
    :FOR    ${server_profile}    IN    @{Syn_edit_gen10_profiles}
    \      ${resp} =     Edit Server Profile    ${server_profile}
    \      Append To List    ${responses}    ${resp}
    Wait For Task2    ${responses}    timeout=2400    interval=15

Login to Fusion via SSH
    [Documentation]    Connect to Fusion VM via SSH
    ...    Example:\n| Login to Fusion Via SSH | 10.0.12.106 | Administrator | hpvse123 |
    [Arguments]    ${IP}=${Syn_fusion_ip}    ${USERNAME}=${Syn_fusion_ssh_username}    ${PASSWORD}=${Syn_fusion_ssh_password}
    Log Many    ${Syn_fusion_ip}    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    ${Id}=    Open Connection    ${Syn_fusion_ip}
    ${Output}=    Login    ${Syn_fusion_ssh_username}    ${Syn_fusion_ssh_password}
    [Return]    ${Id}

Logout of Fusion Via SSH
    [Documentation]    Exits the current SSH session
    ...                Example:\n| Logout Of Fusion Via SSH |
    Close Connection

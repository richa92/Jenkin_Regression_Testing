*** Settings ***
Documentation                   Synergy Server profiles and templates for BIOS TESTING.

Library             FusionLibrary
Library             RoboGalaxyLibrary
Library             OperatingSystem
Library             SSHLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             String
Library             common_functions
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            resources.robot
Variables           ${DATA_FILE}

Suite Setup         Setup
Suite Teardown      Clean Up

*** Variables ***
${APPLIANCE_IP}     ${syn_fusion_ip}
${DATA_FILE}        ./ovs35415_dcs_cdp_bios_data.py

*** Test Cases ***
OVS35415 - Create Assigned Profiles with BIOS Settings
    [Documentation]    Testing the Assigned Profiles with BIOS Settings
    [TAGS]    BIOSOnly
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_bios_only}
    Log     ${prof_list}
    Create Server Profiles     ${prof_list}
    Power on Server and check if its ON     ${syn_server_ilo_hostname}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_bios_only}
    Log     ${prof_list}
    Edit Server Profiles       ${prof_list}
    Delete Server Profiles     ${prof_list}

OVS35415 - Create Assigned Profiles with - F/W and BIOS Settings
    [Documentation]    Testing the Assigned Profiles with Fw and BIOS Settings
    [TAGS]    Firmware
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${dict} =       Add Firmware Baseline Uri To Dict      ${syn_${gen}_server_profile_firmware_and_bios['firmware']}
    Set to Dictionary    ${syn_${gen}_server_profile_firmware_and_bios}    firmware        ${dict}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_firmware_and_bios}
    Log     ${prof_list}
    Create Server Profiles     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_bios_only}
    Log     ${prof_list}
    Edit Server Profiles       ${prof_list}
    Delete Server Profiles     ${prof_list}

OVS35415 - Create Assigned Profiles with - specific attributes
    [Documentation]     Testing the Assigned Profiles with the below given specific attributes
    ...                 # Virualization 158,
    ...                 # Hyperthreading 176,
    ...                 # Turbo Boost performance 181,
    ...                 # VTd 186
    [TAGS]      SpecificAttribs
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_create_specific_bios}
    Log     ${prof_list}
    Create Server Profiles     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_specific_bios}
    Log     ${prof_list}
    Edit Server Profiles       ${prof_list}
    Delete Server Profiles     ${prof_list}

OVS35415 - Create Assigned Profiles with - Server Profile Template and Check if it is Compliant
    [Documentation]     Testing the Assigned Profiles with Server Profile Template and Check if it is Compliant
    [TAGS]      SPT
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${templt_lst} =    Add Sht Name to dict     ${syn_${gen}_profile_templates[0]}
    Create Server Profile Template      ${templt_lst}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_with_template_and_bios}
    Log     ${prof_list}
    Create Server Profiles     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_bios_only}
    Log     ${prof_list}
    Edit Server Profiles       ${prof_list}
    Check Profile if NonCompliant with Template     ${prof_list}
    Delete Server Profiles     ${prof_list}
    Delete Profile Template     ${templt_lst}

OVS35415 - Create Assigned Profiles - with selective re-apply on server hardware
    [Documentation]     Testing the Assigned Profile with selective re-apply on server hardware
    [Tags]      BOOT
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_bootmode_and_bios}
    Log     ${prof_list}
    Create Server Profiles     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_bios_only}
    Log     ${prof_list}
    Edit Server Profiles       ${prof_list}
    Delete Server Profiles     ${prof_list}

OVS35415 - Create UnAssigned Profile with Default BIOS and Assign it to server
    [Documentation]     Testing the UnAssigned Profile with Default BIOS values and assign it to Server
    [Tags]      DefaultBios
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${templt_lst} =    Add Sht Name to dict     ${syn_${gen}_profile_templates[0]}
    Create Server Profile Template      ${templt_lst}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_unassign_defbios}
    Log     ${prof_list}
    Create Server Profiles Unassigned     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_assign_defbios}
    Log     ${prof_list}
    Power Off Server     ${syn_server_ilo_hostname}
    ${power_state}=    Get Server Power    ${syn_server_ilo_hostname}
    Run keyword if    '${power_state}'!='Off'    FAIL    Server power on failed
    Edit Server Profiles       ${prof_list}
    Delete Server Profiles     ${prof_list}

OVS35415 - Create Assigned Profile with Default BIOS and Edit it
    [Documentation]     Testing the Assigned Profile with Default BIOS values and Edit it
    [Tags]      DefaultBiosAssign
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_assign_defbios}
    Create Server Profiles     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_assign_defbios}
    Edit Server Profiles       ${prof_list}
    Delete Server Profiles     ${prof_list}
    
OVS35415 - Create Assigned Profiles - with selective re-apply on profile connection
    [Documentation]     Testing the Assigned Profile with selective re-apply on profile connection
    [Tags]      CONN
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_connection_and_bios}
    Log     ${prof_list}
    Create Server Profiles     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_edit_bios_only}
    Log     ${prof_list}
    Edit Server Profiles       ${prof_list}
    Delete Server Profiles     ${prof_list}

OVS35415 - Create UnAssigned Profiles
    [Documentation]    Testing UnAssigned Profiles
    [TAGS]    UnAssignedProfile
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${prof_lst} =       Add Sht Name to dict     ${syn_${gen}_server_profiles[0]}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_unassign}
    Create Server Profiles Unassigned     ${prof_list}
    ${prof_list} =    Add dicts to list    ${prof_lst[0]}    ${syn_${gen}_server_profile_assign}
    Edit Server Profiles Unassign       ${prof_list}
    Delete Server Profiles     ${prof_list}
    ${templt_lst} =    Add Sht Name to dict     ${syn_${gen}_profile_templates[0]}
    Delete Profile Template     ${templt_lst}

*** Keywords ***
Setup
    [Documentation]    CDP Setup
    Set Log Level  DEBUG
    ${admin_session} =    Fusion Api Login Appliance         ${APPLIANCE_IP}        ${syn_admin_credentials}

Clean Up
    [Documentation]    CDP Teardown
    Fusion Api Logout Appliance

Add Sht Name to dict
    [Documentation]     Adds/Updates the key/value {"serverHardwareTypeUri": "SHT:${sht_name}"} to the given dictionary and returns a list
    [Arguments]     ${given_dict}
    ${sht_name} =   Get Sht Name    ${syn_server_ilo_hostname}
    &{dict} =   Create Dictionary
    ${dict} =   Evaluate    {"serverHardwareTypeUri": "SHT:${sht_name}"}
    ${gen}=    Convert to Lowercase    ${syn_server_genration}
    ${final_lst} =      Add dicts to list      ${given_dict}    ${dict}
    [Return]    ${final_lst}

Add Firmware Baseline Uri To Dict
    [Documentation]     Adds/Updaes the key/value {"firmwareBaselineUri":"/rest/firmwareBaselineUri/..."} to the given dictionary and returns a list
    [Arguments]     ${given_dict}
    ${id}=     Open Connection     ${syn_fusion_ip}
    ${login_output}=     Login    ${syn_fusion_ssh_credentials_username}    ${syn_fusion_ssh_credentials_password}
    ${output}=    Execute Command     /usr/bin/curl -k -s -S -X POST -d '{"userName":"${syn_fusion_admin_credentials_username}", "password":"${syn_fusion_admin_credentials_password}"}' -H "Content-Type: application/json" -H "Accept: application/json" "https://${syn_fusion_ip}/authn/rest/login-sessions" |cut -d'"' -f4
    ${fw_details} =    Execute Command    /usr/bin/curl -k -s -S -X GET -H "x-api-version: ${syn_api_version}" -H "Content-Type: application/json" -H "Accept: application/json" -H "auth:${output}" "https://${syn_fusion_ip}/rest/firmware-drivers"
    &{fw_dict} =     string to dictionary     ${fw_details}
    ${fw_count}=    Get From Dictionary     ${fw_dict}    count
    &{dict} =   Create Dictionary
    :For    ${x}    IN RANGE    0   ${fw_count}
    \   ${fw_iso} =     Get From Dictionary      ${fw_dict['members'][${x}]}    isoFileName
    \   ${fw_uri} =     Get From Dictionary      ${fw_dict['members'][${x}]}    uri
    \   &{new_dict} =       Create Dictionary   firmwareBaselineUri    ${fw_uri}
    \   Log     ${new_dict}
    \   Run Keyword If      "${fw_iso}" == "${syn_firmware_iso_uploaded_into_OneView}"      Set to Dictionary    ${dict}      firmwareBaselineUri      ${fw_uri}
    ${length} =  Get Length    ${dict}
    Run Keyword If    ${length} == 0    log to console    Missing Firmware Bundle
    Should Not Be Equal     '${length}'    '0'
    Set to Dictionary      ${given_dict}       &{dict}
    [Return]    ${given_dict}

Get Sht Name
    [Documentation]     Gets the SHT Name by the given server name
    [Arguments]     ${hostname}
    ${id}=     Open Connection     ${syn_fusion_ip}
    ${output}=     Login    ${syn_fusion_ssh_credentials_username}    ${syn_fusion_ssh_credentials_password}
    ${shturi} =       Get Server Hardware Type URI By Server Hardware       ${hostname}
    ${output}=    Execute Command     /usr/bin/curl -k -s -S -X POST -d '{"userName":"${syn_fusion_admin_credentials_username}", "password":"${syn_fusion_admin_credentials_password}"}' -H "Content-Type: application/json" -H "Accept: application/json" "https://${syn_fusion_ip}/authn/rest/login-sessions" |cut -d'"' -f4
    ${sht_dict} =    Execute Command    /usr/bin/curl -k -s -S -X GET -H "x-api-version: ${syn_api_version}" -H "Content-Type: application/json" -H "Accept: application/json" -H "auth:${output}" "https://${syn_fusion_ip}${shturi}"
    &{sht_dict} =     string to dictionary     ${sht_dict}
    ${sht_name}=    Get From Dictionary     ${sht_dict}    name
    [Return]    ${sht_name}
    Close Connection

Check Profile if NonCompliant with Template
    [Documentation]    CDP After Creating and Editing the Server Profile and Templates, Checks if the Template and Profile are Non-Compliant.
    [Arguments]     ${profiles}
    ${id}=     Open Connection     ${syn_fusion_ip}
    ${output}=     Login    ${syn_fusion_ssh_credentials_username}    ${syn_fusion_ssh_credentials_password}
    ${output}=    Execute Command     /usr/bin/curl -k -s -S -X POST -d '{"userName":"${syn_fusion_admin_credentials_username}", "password":"${syn_fusion_admin_credentials_password}"}' -H "Content-Type: application/json" -H "Accept: application/json" "https://${syn_fusion_ip}/authn/rest/login-sessions" |cut -d'"' -f4
    &{prof_dict}=     Get From List     ${profiles}     0
    ${prof_name}=     Get From Dictionary     ${prof_dict}     name
    ${svr_prof_uri}=     Get Server Profile URI     ${prof_name}
    ${ProfDetails} =    Execute Command    /usr/bin/curl -k -s -S -X GET -H "x-api-version: ${syn_api_version}" -H "Content-Type: application/json" -H "Accept: application/json" -H "auth:${output}" "https://${syn_fusion_ip}${svr_prof_uri}"
    &{prof_dict} =     string to dictionary     ${ProfDetails}
    ${temp_compliant}=    Get From Dictionary     ${prof_dict}    templateCompliance
    Should Not Be Equal     ${temp_compliant}     NonCompliant
    Close Connection

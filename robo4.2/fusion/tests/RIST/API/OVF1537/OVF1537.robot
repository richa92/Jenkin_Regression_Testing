*** Settings ***
Documentation       OVF1537 - SP API to regenerate CHAP/MCHAP credentials (secrets) to achieve security compliance for renewing passwords
Library				FusionLibrary
Library  			BuiltIn
Library				Collections
Library             json
Library  			Dialogs
Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Login the Appliance
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Remove all Profiles and Templates
...                 AND     Create the Server Profile

Suite Teardown      Run Keywords    Remove all Profiles and Templates
...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${DATA_FILE}         Regression_Data.py
#${X_API_VERSION}     500

*** Test Cases ***

TS1 Verify Regeneration of MCHAP Credentials on Single Volume
    ${old_secretsGenerated}=  Get Server Profile secretsGenerated  ${profile1}
    ${credlist}=  Get Server Profile SAN Storage Credentials  ${profile1}
    ${old_sanStorageCredentials}=  Get SAN Storage Credentials  ${credlist}  StorageSystemV4:${STOREVIRTUAL_SLPT_STATIC_STORAGE_SYSTEM}
    ${volume1_attachments}=  Get Storage Volume Attachments for Profile and Volume  ${PROFILE1_NAME}  ${STOREVIRTUAL_VOLUME1_NAME}
    Verify CHAP Secrets Against Volume Attachment  ${old_sanStorageCredentials}  ${volume1_attachments}
    ${task}=  Patch Server Profile  ${profile1}  op=replace  path=/sanstorage/regenerateChapSecrets    value=ExcludeValue
    Wait for task2  ${task}  timeout=300  interval=3
    ${new_secretsGenerated}=  Get Server Profile secretsGenerated  ${profile1}
    ${credlist}=  Get Server Profile SAN Storage Credentials  ${profile1}
    ${new_sanStorageCredentials}=  Get SAN Storage Credentials  ${credlist}  StorageSystemV4:${STOREVIRTUAL_SLPT_STATIC_STORAGE_SYSTEM}
    Run Keyword If  "${old_secretsGenerated}" == "${new_secretsGenerated}"  Fail  secretsGenerated timestamp not updated after regeneration request
    Run Keyword If  "${old_sanStorageCredentials['chapSecret']}" == "${new_sanStorageCredentials['chapSecret']}"  Fail  CHAP secret unchanged after regeneration request
    Run Keyword If  "${old_sanStorageCredentials['mutualChapSecret']}" == "${new_sanStorageCredentials['mutualChapSecret']}"  Fail  MCHAP secret unchanged after regeneration request
    ${volume1_attachments}=  Get Storage Volume Attachments for Profile and Volume  ${PROFILE1_NAME}  ${STOREVIRTUAL_VOLUME1_NAME}
    Verify CHAP Secrets Against Volume Attachment  ${new_sanStorageCredentials}  ${volume1_attachments}

TS1 Add Volume On Second Storage Device and Verify Unchanged secretsGenerated
    ${old_secretsGenerated}=  Get Server Profile secretsGenerated  ${profile1}
    ${task}=  Edit Server Profile  ${edit_profile1}
    Wait for task2  ${task}  timeout=300  interval=3
    ${new_secretsGenerated}=  Get Server Profile secretsGenerated  ${profile1}
    Run Keyword If  "${old_secretsGenerated}" != "${new_secretsGenerated}"  Fail  secretsGenerated timestamp updated after adding second volume on second storage device

TS1 Verify Regeneration of MCHAP Credentials on Multiple Volumes
    ${old_secretsGenerated}=  Get Server Profile secretsGenerated  ${profile1}
    ${credlist}=  Get Server Profile SAN Storage Credentials  ${profile1}
    ${old_sanStorageCredentials1}=  Get SAN Storage Credentials  ${credlist}  StorageSystemV4:${STOREVIRTUAL_SLPT_STATIC_STORAGE_SYSTEM}
    ${old_sanStorageCredentials2}=  Get SAN Storage Credentials  ${credlist}  StorageSystemV4:${STOREVIRTUAL_SLPT_DHCP_STORAGE_SYSTEM}
    ${volume1_attachments}=  Get Storage Volume Attachments for Profile and Volume  ${PROFILE1_NAME}  ${STOREVIRTUAL_VOLUME1_NAME}
    ${volume2_attachments}=  Get Storage Volume Attachments for Profile and Volume  ${PROFILE1_NAME}  ${STOREVIRTUAL_VOLUME2_NAME}
    Verify CHAP Secrets Against Volume Attachment  ${old_sanStorageCredentials1}  ${volume1_attachments}
    Verify CHAP Secrets Against Volume Attachment  ${old_sanStorageCredentials2}  ${volume2_attachments}
    ${task}=  Patch Server Profile  ${profile1}  op=replace  path=/sanstorage/regenerateChapSecrets    value=ExcludeValue
    Wait for task2  ${task}  timeout=300  interval=3
    ${new_secretsGenerated}=  Get Server Profile secretsGenerated  ${profile1}
    ${credlist}=  Get Server Profile SAN Storage Credentials  ${profile1}
    ${new_sanStorageCredentials1}=  Get SAN Storage Credentials  ${credlist}  StorageSystemV4:${STOREVIRTUAL_SLPT_STATIC_STORAGE_SYSTEM}
    ${new_sanStorageCredentials2}=  Get SAN Storage Credentials  ${credlist}  StorageSystemV4:${STOREVIRTUAL_SLPT_DHCP_STORAGE_SYSTEM}
    Run Keyword If  "${old_secretsGenerated}" == "${new_secretsGenerated}"  Fail  secretsGenerated timestamp not updated after regeneration request
    Run Keyword If  "${old_sanStorageCredentials1['chapSecret']}" == "${new_sanStorageCredentials1['chapSecret']}"  Fail  CHAP secret unchanged on volume 1 after regeneration request
    Run Keyword If  "${old_sanStorageCredentials1['mutualChapSecret']}" == "${new_sanStorageCredentials1['mutualChapSecret']}"  Fail  MCHAP secret unchanged on volume 1 after regeneration request
    Run Keyword If  "${old_sanStorageCredentials2['chapSecret']}" == "${new_sanStorageCredentials2['chapSecret']}"  Fail  CHAP secret unchanged on volume 2 after regeneration request
    Run Keyword If  "${old_sanStorageCredentials2['mutualChapSecret']}" == "${new_sanStorageCredentials2['mutualChapSecret']}"  Fail  MCHAP secret unchanged on volume 2 after regeneration request
    ${volume1_attachments}=  Get Storage Volume Attachments for Profile and Volume  ${PROFILE1_NAME}  ${STOREVIRTUAL_VOLUME1_NAME}
    ${volume2_attachments}=  Get Storage Volume Attachments for Profile and Volume  ${PROFILE1_NAME}  ${STOREVIRTUAL_VOLUME2_NAME}
    Verify CHAP Secrets Against Volume Attachment  ${new_sanStorageCredentials1}  ${volume1_attachments}
    Verify CHAP Secrets Against Volume Attachment  ${new_sanStorageCredentials2}  ${volume2_attachments}

TS1 Verify Regeneration Denied on Older API
    ${task}=  Patch Server Profile  ${profile1}  api=500  op=replace  path=/sanstorage/regenerateChapSecrets    value=ExcludeValue
    Wait for task2  ${task}  timeout=300  interval=3  PASS=Error  errorMessage=PATCH_not_supported

TS1 Verify Regeneration Denied on Powered On Server
    Power On Server  ${profile1['serverHardwareUri']}
    ${task}=  Patch Server Profile  ${profile1}  op=replace  path=/sanstorage/regenerateChapSecrets    value=ExcludeValue
    Wait for task2  ${task}  timeout=300  interval=3  PASS=Error  errorMessage=Cannot_regenerate_CHAP_unless_server_powered_off

*** Keywords ***
Login the Appliance
    [Documentation]  Set the log level, log the variables and login to the appliance as Administrator
    Set Log Level	TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Power off all servers, remove all SP's and, remove all SPT's
    Power off ALL servers
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

Create the Server Profile
    [Documentation]  Create the initial Server Profile for testing
    Power Off Server  ${profile1['serverHardwareUri']}
    ${resp}=  Add Server Profile  ${profile1}
    Wait for task2  ${resp}  timeout=300  interval=3

Get Server Profile secretsGenerated
    [Documentation]  Given a profile, return the secretsRegenerated timestamp
    [Arguments]      ${profile}
    ${profile_dto} =  Get Resource  SP:${profile['name']}
    [Return]  ${profile_dto['sanStorage']['secretsGenerated']}

Get Server Profile SAN Storage Credentials
    [Documentation]  Given a profile, return the sanSystemCredentials list
    [Arguments]      ${profile}
    ${profile_dto} =  Get Resource  SP:${profile['name']}
    [Return]  ${profile_dto['sanStorage']['sanSystemCredentials']}

Get SAN Storage Credentials
    [Documentation]  Return the SAN storage credentials for a SAN storage system URI
    [Arguments]  ${credential_list}  ${storage_uri}
    ${storage_system_uri}=  Common URI lookup by name  ${storage_uri}
    :FOR  ${credential}  in  @{credential_list}
    \   Return From Keyword If  '${credential['storageSystemUri']}' == '${storage_system_uri}'  ${credential}
    Log    "Cannot find SAN Storage Credentials for ${storage_system_uri}"    console=true
    [Return]  ${None}

Get Storage Volume Attachments for Profile and Volume
    [Documentation]  Given a profile name and volume name, return the volume attachments list from StRM representing storage state
    [Arguments]  ${profile_name}  ${volume_name}
    ${profile_uri}=  Common URI lookup by name  SP:${profile_name}
    ${volume_uri}=  Common URI lookup by name  SVOL:${volume_name}
    ${volume_attachments}=  Get Resource by URI  /rest/storage-volume-attachments
    :FOR  ${member}  in  @{volume_attachments['members']}
    \  Return From Keyword If  '${member['ownerUri']}' == '${profile_uri}' and '${member['storageVolumeUri']}' == '${volume_uri}'  ${member}
    Log    "Cannot find Storage Volume Attachments for ${profile_name}/${volume_name}"    console=true
    [Return]  ${None}

Verify CHAP Secrets Against Volume Attachment
    [Documentation]  Given a sanSystemCredentials struct from a profile and a volume attachment member struct, verify CHAP/MCHAP secrets
    ...              volume attachment is from StRM, represents storage device state, not server state
    [Arguments]  ${sanSystemCredentials}  ${volume_attachment}
    :FOR  ${path}  in  @{volume_attachment['paths']}
    \  Run Keyword If  "${path['initiator']['chap']['secret']}" != "${sanSystemCredentials['chapSecret']}" or "${path['initiator']['mutualChap']['secret']}" != "${sanSystemCredentials['mutualChapSecret']}"  Fail  Profile CHAP secrets do not match storage
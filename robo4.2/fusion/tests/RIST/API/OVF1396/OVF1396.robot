*** Settings ***
Documentation       OVF1396 - Completer for OVF734 designation of CHAP Level (None, CHAP, MCHAP) for iSCSI volume
...                 attachments, and do CHAP Level compliance checks (SP and SPT)
...                 Requires X-API-VERSION >= 1000

Library             FusionLibrary
Library             BuiltIn
Library             Collections

Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt

Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
Suite Teardown      Fusion Api Logout Appliance

*** Variables ***

*** Test Cases ***

OVF1396 TS1 - Varying Server Profile Template CHAP Levels
    [Tags]  SPT  TS1
    Log  .  console=True
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile Template  ${ts1_spt_0_storevirtual}
    Wait For Task2  ${task}  timeout=300  interval=2

    ${my_spt} =  Copy Dictionary  ${ts1_spt_1_storevirtual}
    :FOR  ${chap_level}  IN  @{CHAP_LEVELS}
    \   Initialize Appliance For Test Case
    \   Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=${chap_level}
    \   ${task}=  Add Server Profile Template  ${my_spt}
    \   Wait For Task2  ${task}  timeout=300  interval=2
    \   ${uri} =  Get Server Profile Template URI  ${my_spt['name']}
    \   ${created_spt} =  Get Resource by URI  ${uri}
    \   ${original_ssc} =  Lookup sanSystemCredentials uris  ${my_spt['sanStorage']['sanSystemCredentials']}
    \   Compare sanSystemCredentials  ${original_ssc}  ${created_spt['sanStorage']['sanSystemCredentials']}
    \   ${task} =  Remove Server Profile Template  ${my_spt}
    \   Wait For Task2  ${task}  timeout=300  interval=2

    ${my_spt} =  Copy Dictionary  ${ts1_spt_2_storevirtual}
    :FOR  ${chap_level}  IN  @{CHAP_LEVELS}
    \   Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=${chap_level}
    \   Test SPT Create Second Volume CHAP Levels  ${my_spt}

OVF1396 TS2 - Varying Server Profile CHAP Levels
    [Tags]  SP  TS2
    Log  .  console=True
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile  ${ts2_sp_0_storevirtual}
    Wait For Task2  ${task}  timeout=600  interval=10
    SP Compliance is Unknown  ${SP1_NAME}
    # StoreVirtual default level is MutualChap if not specified in SP
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap

    ${my_sp} =  Copy Dictionary  ${ts2_sp_1_storevirtual}

    :FOR  ${chap_level}  IN  @{CHAP_LEVELS}
    \   Initialize Appliance For Test Case
    \   Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][0]}  chapLevel=${chap_level}
    \   ${task}=  Add Server Profile  ${my_sp}
    \   Wait For Task2  ${task}  timeout=600  interval=10
    \   SP Compliance is Unknown  ${SP1_NAME}
    \   SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  ${chap_level}

    ${my_sp} =  Copy Dictionary  ${ts2_sp_2_storevirtual}

    Initialize Appliance For Test Case
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][0]}  chapLevel=None
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][1]}  chapLevel=MutualChap
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Unknown  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  None  MutualChap

    Initialize Appliance For Test Case
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][0]}  chapLevel=Chap
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][1]}  chapLevel=Chap
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Unknown  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  Chap  Chap

    Initialize Appliance For Test Case
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][0]}  chapLevel=MutualChap
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][1]}  chapLevel=None
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Unknown  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  None

OVF1396 TS3 - Create Server Profile From Server Profile Template and Check for Consistent CHAP Levels
    [Tags]  SPT  SP  TS3
    Log  .  console=True
    Initialize Appliance For Test Case
    ${my_spt} =  Copy Dictionary  ${ts1_spt_2_storevirtual}

    # pass 1 with MutualChap/Chap
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=MutualChap
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][1]}  chapLevel=Chap
    ${task}=  Add Server Profile Template  ${my_spt}
    Wait For Task2  ${task}  timeout=300  interval=10
    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  Chap

    # pass 2 with Chap/None
    Initialize Appliance For Test Case
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=Chap
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][1]}  chapLevel=None
    ${task}=  Add Server Profile Template  ${my_spt}
    Wait For Task2  ${task}  timeout=300  interval=10
    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  Chap  None

    # pass 3 with MutualChap/MutualChap
    Initialize Appliance For Test Case
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=MutualChap
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][1]}  chapLevel=MutualChap
    ${task}=  Add Server Profile Template  ${my_spt}
    Wait For Task2  ${task}  timeout=300  interval=10
    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  MutualChap

OVF1396 TS4 - Server Profile CHAP Level Edits
    [Tags]  SP  TS4  OVD23763
    Log  .  console=True
    Initialize Appliance For Test Case

    # create the initial SP from SPT
    ${my_spt} =  Copy Dictionary  ${ts1_spt_2_storevirtual}
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=None
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][1]}  chapLevel=MutualChap
    ${task}=  Add Server Profile Template  ${my_spt}
    Wait For Task2  ${task}  timeout=300  interval=10
    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  None  MutualChap

    # pass 1  change sanSystemCredentials CHAP level for volumes on StoreVirtual 1
    Change SP CHAP Levels  ${SP1_NAME}  chap1=Chap
    SP Compliance is NonCompliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  Chap  MutualChap

    # pass 2  change sanSystemCredentials CHAP level for volumes on StoreVirtual 2
    Change SP CHAP Levels  ${SP1_NAME}  chap2=None
    SP Compliance is NonCompliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  Chap  None

    # pass 3  change sanSystemCredentials CHAP level for volumes on StoreVirtual 1 and 2
    Change SP CHAP Levels  ${SP1_NAME}  chap1=MutualChap  chap2=Chap
    SP Compliance is NonCompliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  Chap

    # pass 4  bring SP back to SPT compliant CHAP levels
    Change SP CHAP Levels  ${SP1_NAME}  chap1=None  chap2=MutualChap
    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  None  MutualChap

OVF1396 TS5 - CHAP Level Compliance Checks
    [Tags]  SPT  SP  TS5
    Log  .  console=True
    Initialize Appliance For Test Case

    ${my_spt} =  Copy Dictionary  ${ts1_spt_2_storevirtual}
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=MutualChap
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][1]}  chapLevel=Chap
    ${task}=  Add Server Profile Template  ${my_spt}
    Wait For Task2  ${task}  timeout=300  interval=10

    Set to Dictionary  ${my_spt}  name=${SPT2_NAME}
    ${task}=  Add Server Profile Template  ${my_spt}
    Wait For Task2  ${task}  timeout=300  interval=10

    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Add Server Profile  ${SP2_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  Chap
    SP Compliance is Compliant  ${SP2_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP2_NAME}  MutualChap  Chap

    #  Change SP CHAP Level and verify compliance alert is created for that SP and not other SPs associated with the same SPT
    Change SP CHAP Levels  ${SP1_NAME}  chap2=MutualChap
    SP Compliance is NonCompliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  MutualChap
    SP Compliance is Compliant  ${SP2_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP2_NAME}  MutualChap  Chap

    # Change SPT CHAP Level and verify compliance alert is created or cleared for each associated SP
    Change SPT CHAP Levels  ${SPT1_NAME}  MutualChap  MutualChap
    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  MutualChap
    SP Compliance is NonCompliant  ${SP2_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP2_NAME}  MutualChap  Chap

    # Validate that removing the SPT association to a SP clears any prior compliance alerts on the SP
    ${sp}=  Get Resource  SP:${SP2_NAME}
    Set to Dictionary  ${sp}  serverProfileTemplateUri=${None}
    Remove From Dictionary  ${sp}  status_code  headers
    ${uri} =    Common URI lookup by name    SP:${SP2_NAME}
    ${task} =    Fusion Api Edit Server Profile   body=${sp}    uri=${uri}
    Wait For Task2  ${task}  timeout=60  interval=2

    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  MutualChap
    SP Compliance is Unknown  ${SP2_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP2_NAME}  MutualChap  Chap

    # Validate that SP changed to be associated with a different SPT will run the compliance checks
    ${sp}=  Get Resource  SP:${SP2_NAME}
    ${uri}=  Common URI lookup by name  SPT:${SPT2_NAME}
    Set to Dictionary  ${sp}  serverProfileTemplateUri=${uri}

    ${spt}=  Get Resource  SPT:${SPT2_NAME}

    ${spv}=  Get Volume by ID  ${sp['sanStorage']['volumeAttachments']}  1
    ${sptv}=  Get Volume by ID  ${spt['sanStorage']['volumeAttachments']}  1
    Set to Dictionary  ${spv}  associatedTemplateAttachmentId=${sptv['associatedTemplateAttachmentId']}

    ${spv}=  Get Volume by ID  ${sp['sanStorage']['volumeAttachments']}  2
    ${sptv}=  Get Volume by ID  ${spt['sanStorage']['volumeAttachments']}  2
    Set to Dictionary  ${spv}  associatedTemplateAttachmentId=${sptv['associatedTemplateAttachmentId']}

    ${spv}=  Get Volume by ID  ${sp['sanStorage']['volumeAttachments']}  3
    ${sptv}=  Get Volume by ID  ${spt['sanStorage']['volumeAttachments']}  3
    Set to Dictionary  ${spv}  associatedTemplateAttachmentId=${sptv['associatedTemplateAttachmentId']}

    Remove From Dictionary  ${sp}  status_code  headers
    ${uri} =    Common URI lookup by name    SP:${SP2_NAME}
    ${task} =    Fusion Api Edit Server Profile   body=${sp}    uri=${uri}
    Wait For Task2  ${task}  timeout=60  interval=2

    SP Compliance is Compliant  ${SP2_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP2_NAME}  MutualChap  Chap

OVF1396 TS6 - Automatic Remediation of New SPT volume
    [Tags]  SPT  SP  TS6
    [Documentation]  Verify automatic addition of new storage system volume to SP from its SPT.
    ...              New volume should use CHAP settings from the SPT, not the StoreVirtual default of MutualChap
    Log  .  console=True
    Initialize Appliance For Test Case

    ${task}=  Add Server Profile Template  ${ts6_spt_create}
    Wait For Task2  ${task}  timeout=300  interval=10

    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10
    SP Compliance is Compliant  ${SP1_NAME}

    ${task}=  Edit Server Profile Template  ${ts6_spt_edit}
    Wait For Task2  ${task}  timeout=300  interval=10

    SP Compliance is NonCompliant  ${SP1_NAME}
    ${sp}=  Get Resource  SP:${SP1_NAME}
    ${cp}=  Get Resource  ${sp['uri']}/compliance-preview
    ${mulen}=  Get Length  ${cp['manualUpdates']}
    Should Be Equal as Integers  ${mulen}  0
    ${aulen}=  Get Length  ${cp['automaticUpdates']}
    Should Be Equal as Integers  ${aulen}  2
    ${sv}=  Get Resource  SSYS:${STOREVIRTUAL_2_SYSTEM_NAME}
    List Should Contain Value  ${cp['automaticUpdates']}  Create an attachment to a new volume "${VOLUME_SV2_1_NAME}".
    List Should Contain Value  ${cp['automaticUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_2_SYSTEM_NAME}", "uri":"${sv['uri']}"} to use CHAP level Chap.
    ${task}=  Patch Server Profile  ${sp}  # default behavior is to request SPT compliance
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Compliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  Chap

OVF1396 TS7 - Manual SP Remediation For CHAP level upgrades and downgrades
    [Tags]  SPT  SP  TS7
    [Documentation]  All SPT CHAP level upgrades and downgrades should raise a noncompliant SP with manual remediation required
    Log  .  console=True
    Initialize Appliance For Test Case

    ${sv1}=  Get Resource  SSYS:${STOREVIRTUAL_1_SYSTEM_NAME}
    ${sv2}=  Get Resource  SSYS:${STOREVIRTUAL_2_SYSTEM_NAME}

    ${my_spt} =  Copy Dictionary  ${ts1_spt_2_storevirtual}
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][0]}  chapLevel=MutualChap
    Set to Dictionary  ${my_spt['sanStorage']['sanSystemCredentials'][1]}  chapLevel=Chap
    ${task}=  Add Server Profile Template  ${my_spt}
    Wait For Task2  ${task}  timeout=300  interval=10

    # Downgrade MutualChap->Chap and Chap->None
    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10
    SP Compliance is Compliant  ${SP1_NAME}

    Change SPT CHAP Levels  ${SPT1_NAME}  Chap  None

    SP Compliance is NonCompliant  ${SP1_NAME}
    ${sp}=  Get Resource  SP:${SP1_NAME}
    ${cp}=  Get Resource  ${sp['uri']}/compliance-preview
    ${mulen}=  Get Length  ${cp['manualUpdates']}
    Should Be Equal as Integers  ${mulen}  2
    ${aulen}=  Get Length  ${cp['automaticUpdates']}
    Should Be Equal as Integers  ${aulen}  0

    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_1_SYSTEM_NAME}", "uri":"${sv1['uri']}"} to use CHAP level Chap.
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_2_SYSTEM_NAME}", "uri":"${sv2['uri']}"} to use CHAP level None.

    ${task}=  Patch Server Profile  ${sp}  # default behavior is to request SPT compliance
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail

    SP Compliance is NonCompliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  Chap
    ${sp}=  Get Resource  SP:${SP1_NAME}
    ${cp}=  Get Resource  ${sp['uri']}/compliance-preview
    ${mulen}=  Get Length  ${cp['manualUpdates']}
    Should Be Equal as Integers  ${mulen}  2
    ${aulen}=  Get Length  ${cp['automaticUpdates']}
    Should Be Equal as Integers  ${aulen}  0
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_1_SYSTEM_NAME}", "uri":"${sv1['uri']}"} to use CHAP level Chap.
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_2_SYSTEM_NAME}", "uri":"${sv2['uri']}"} to use CHAP level None.

    # Downgrade MutuaChap->None, upgrade None->Chap
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10
    Change SPT CHAP Levels  ${SPT1_NAME}  MutualChap  None
    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    Change SPT CHAP Levels  ${SPT1_NAME}  None  Chap

    SP Compliance is NonCompliant  ${SP1_NAME}
    ${sp}=  Get Resource  SP:${SP1_NAME}
    Should Be Equal  ${sp['templateCompliance']}  NonCompliant
    ${cp}=  Get Resource  ${sp['uri']}/compliance-preview
    ${mulen}=  Get Length  ${cp['manualUpdates']}
    Should Be Equal as Integers  ${mulen}  2
    ${aulen}=  Get Length  ${cp['automaticUpdates']}
    Should Be Equal as Integers  ${aulen}  0
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_1_SYSTEM_NAME}", "uri":"${sv1['uri']}"} to use CHAP level None.
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_2_SYSTEM_NAME}", "uri":"${sv2['uri']}"} to use CHAP level Chap.

    ${task}=  Patch Server Profile  ${sp}  # default behavior is to request SPT compliance
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail

    SP Compliance is NonCompliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  MutualChap  None
    ${sp}=  Get Resource  SP:${SP1_NAME}
    ${cp}=  Get Resource  ${sp['uri']}/compliance-preview
    ${mulen}=  Get Length  ${cp['manualUpdates']}
    Should Be Equal as Integers  ${mulen}  2
    ${aulen}=  Get Length  ${cp['automaticUpdates']}
    Should Be Equal as Integers  ${aulen}  0
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_1_SYSTEM_NAME}", "uri":"${sv1['uri']}"} to use CHAP level None.
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_2_SYSTEM_NAME}", "uri":"${sv2['uri']}"} to use CHAP level Chap.

    # Upgrade Chap->MutualChap, None->MutualChap
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10
    Change SPT CHAP Levels  ${SPT1_NAME}  Chap  None
    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    Change SPT CHAP Levels  ${SPT1_NAME}  MutualChap  MutualChap

    SP Compliance is NonCompliant  ${SP1_NAME}
    ${sp}=  Get Resource  SP:${SP1_NAME}
    Should Be Equal  ${sp['templateCompliance']}  NonCompliant
    ${cp}=  Get Resource  ${sp['uri']}/compliance-preview
    ${mulen}=  Get Length  ${cp['manualUpdates']}
    Should Be Equal as Integers  ${mulen}  2
    ${aulen}=  Get Length  ${cp['automaticUpdates']}
    Should Be Equal as Integers  ${aulen}  0
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_1_SYSTEM_NAME}", "uri":"${sv1['uri']}"} to use CHAP level MutualChap.
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_2_SYSTEM_NAME}", "uri":"${sv2['uri']}"} to use CHAP level MutualChap.

    ${task}=  Patch Server Profile  ${sp}  # default behavior is to request SPT compliance
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail

    SP Compliance is NonCompliant  ${SP1_NAME}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${SP1_NAME}  Chap  None
    ${sp}=  Get Resource  SP:${SP1_NAME}
    ${cp}=  Get Resource  ${sp['uri']}/compliance-preview
    ${mulen}=  Get Length  ${cp['manualUpdates']}
    Should Be Equal as Integers  ${mulen}  2
    ${aulen}=  Get Length  ${cp['automaticUpdates']}
    Should Be Equal as Integers  ${aulen}  0
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_1_SYSTEM_NAME}", "uri":"${sv1['uri']}"} to use CHAP level MutualChap.
    List Should Contain Value  ${cp['manualUpdates']}  Configure the volume attachment(s) of storage system {"name":"${STOREVIRTUAL_2_SYSTEM_NAME}", "uri":"${sv2['uri']}"} to use CHAP level MutualChap.

OVF1396 TS8 - Create SPT From SP, Recreate SP From SPT, and Verify SP
    [Tags]  SPT  SP  TS8
    Initialize Appliance For Test Case

    ${my_sp}=  Copy Dictionary  ${ts2_sp_2_storevirtual}
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][0]}  chapLevel=MutualChap
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][1]}  chapLevel=Chap
    ${task}=  Add Server Profile  ${my_sp}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${sp}=  Get Resource   SP:${my_sp['name']}
    ${spt}=  Get Resource  ${sp['uri']}/new-profile-template

    Remove From Dictionary  ${spt}  status_code  headers
    Set To Dictionary  ${spt}  name=${SPT1_NAME}
    ${task} =  Fusion Api Create Server Profile Template    body=${spt}
    Wait For Task2  ${task}  timeout=300  interval=10

    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10

    ${task}=  Add Server Profile  ${SP1_FROM_SPT1}
    Wait For Task2  ${task}  timeout=600  interval=10

    SP Compliance is Compliant  ${my_sp['name']}
    SP Volumes CHAP Settings Should Match Storage CHAP Settings  ${my_sp['name']}  MutualChap  Chap

OVF1396 TS9 - Bad CHAP levels
    [Tags]  SP  TS9
    Initialize Appliance For Test Case
    ${my_sp}=  Copy Dictionary  ${ts2_sp_2_storevirtual}
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][0]}  chapLevel=MutaulChap
    Set to Dictionary  ${my_sp['sanStorage']['sanSystemCredentials'][1]}  chapLevel=Chip
    ${task}=  Add Server Profile  ${my_sp}
    ${status}  ${return}=  Run Keyword and Ignore Error  Wait For Task2  ${task}  timeout=600  interval=10
    Run Keyword If  '${status}' == 'PASS'  Fail

*** Keywords ***
Change SPT CHAP Levels
    [Documentation]  Change the CHAP levels in an existing SPT
    [Arguments]  ${spt_name}  ${chap1}  ${chap2}
    ${spt}=  Get Resource  SPT:${spt_name}
    ${vol}=  Get Volume by ID  ${spt['sanStorage']['volumeAttachments']}  1
    ${sscred}=  Get sanStorageCredential by URI  ${spt['sanStorage']['sanSystemCredentials']}  ${vol['volumeStorageSystemUri']}
    Set to Dictionary  ${sscred}  chapLevel=${chap1}
    ${vol}=  Get Volume by ID  ${spt['sanStorage']['volumeAttachments']}  3
    ${sscred}=  Get sanStorageCredential by URI  ${spt['sanStorage']['sanSystemCredentials']}  ${vol['volumeStorageSystemUri']}
    Set to Dictionary  ${sscred}  chapLevel=${chap2}
    Remove From Dictionary  ${spt}  status_code  headers
    ${uri} =    Common URI lookup by name    SPT:${spt_name}
    ${task} =    Fusion Api Edit Server Profile Template   body=${spt}    uri=${uri}
    Wait For Task2  ${task}  timeout=60  interval=2

Change SP CHAP Levels
    [Documentation]  Change the CHAP levels in an existing SP
    [Arguments]  ${sp_name}  ${chap1}=notSpecified  ${chap2}=notSpecified
    ${sp}=  Get Resource  SP:${sp_name}

    ${sp_vol}=  Get Volume by ID  ${sp['sanStorage']['volumeAttachments']}  1
    ${sp_sscred}=  Get sanStorageCredential by URI  ${sp['sanStorage']['sanSystemCredentials']}  ${sp_vol['volumeStorageSystemUri']}
    Run Keyword If  '${chap1}' != 'notSpecified'  Set to Dictionary  ${sp_sscred}  chapLevel=${chap1}
    Remove From Dictionary  ${sp_sscred}  chapName  chapSecret  mutualChapName  mutualChapSecret

    ${sp_vol}=  Get Volume by ID  ${sp['sanStorage']['volumeAttachments']}  3
    ${sp_sscred}=  Get sanStorageCredential by URI  ${sp['sanStorage']['sanSystemCredentials']}  ${sp_vol['volumeStorageSystemUri']}
    Run Keyword If  '${chap2}' != 'notSpecified'  Set to Dictionary  ${sp_sscred}  chapLevel=${chap2}
    Remove From Dictionary  ${sp_sscred}  chapName  chapSecret  mutualChapName  mutualChapSecret

    # check for rejection of Edit without ignoreSANWarnings URI flag
    Remove From Dictionary  ${sp}  status_code  headers
    ${task} =    Fusion Api Edit Server Profile    body=${sp}    uri=${sp['uri']}
    Wait For Task2  ${task}  timeout=60  interval=2  PASS=Error

    # Edit with ignoreSANWarnings URI flag
    ${task} =    Fusion Api Edit Server Profile    body=${sp}    uri=${sp['uri']}?force=ignoreSANWarnings
    Wait For Task2  ${task}  timeout=60  interval=2

volumeAttachments Index
    [Documentation]  Given a list of volumeAttachments and an id, return the index in the list
    [Arguments]  ${vol_attachments}  ${id}
    ${index}=  Set Variable  ${0}
    :FOR  ${va}  IN  @{vol_attachments}
    \    Return From Keyword If    '${va['id']}' == '${id}'    ${index}
    \    ${index} =    Set Variable    ${index + 1}
    [Return]  ${None}

sanSystemsCredentials Index
    [Documentation]  Given a list of sanSystemCredentials and an id, return the index in the list
    [Arguments]  ${ss_credentials}  ${uri}
    ${index}=  Set Variable  ${0}
    :FOR  ${sscred}  IN  @{ss_credentials}
    \    Return From Keyword If    '${sscred['storageSystemUri']}' == '${uri}'    ${index}
    \    ${index} =    Set Variable    ${index + 1}
    [Return]  ${None}

Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Initialize Appliance For Test Case
    [Documentation]  Initialize the appliance state
    Power Off Server  SH:${SERVER_GEN9_1}
    Power Off Server  SH:${SERVER_GEN9_2}
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris}
    Wait For Task2  ${task}  timeout=600  interval=10
    ${spt}=  Create Dictionary  name=${SPT1_NAME}
    Remove Server Profile Template If Exists  ${spt}
    Set To Dictionary  ${spt}  name=${SPT2_NAME}
    Remove Server Profile Template If Exists  ${spt}
    Set To Dictionary  ${spt}  name=${SPT1_1SV_NAME}
    Remove Server Profile Template If Exists  ${spt}

Test SPT Create Second Volume CHAP Levels
    [Documentation]  Given a SPT with 2 volumes, sequence through all valid CHAP levels on the second volume creating SPT for each
    [Arguments]  ${spt}
    :FOR  ${chap_level}  IN  @{CHAP_LEVELS}
    \   Initialize Appliance For Test Case
    \   Set to Dictionary  ${spt['sanStorage']['sanSystemCredentials'][1]}  chapLevel=${chap_level}
    \   ${task}=  Add Server Profile Template  ${spt}
    \   Wait For Task2  ${task}  timeout=300  interval=2
    \   ${uri} =  Get Server Profile Template URI  ${spt['name']}
    \   ${created_spt} =  Get Resource by URI  ${uri}
    \   ${original_ssc} =  Lookup sanSystemCredentials uris  ${spt['sanStorage']['sanSystemCredentials']}
    \   Compare sanSystemCredentials  ${original_ssc}  ${created_spt['sanStorage']['sanSystemCredentials']}

Remove Server Profile Template If Exists
    [Documentation]  Remove an existing SPT, otherwise just return
    [Arguments]  ${spt}
    ${status}  ${task} =  Run Keyword and Ignore Error  Remove Server Profile Template  ${spt}
    Run Keyword If  '${status}'=='PASS' and ${task['status_code']}!=404  Wait For Task2  ${task}  timeout=300  interval=2

Get sanStorageCredential by URI
    [Documentation]  Given a list of SanStorageCredentials, return the dictionary element with the specified URI
    [Arguments]  ${sanStorageCredentials}  ${uri}
    :FOR  ${ssc}  IN  @{sanStorageCredentials}
    \   Return From Keyword If  '${ssc['storageSystemUri']}' == '${uri}'  ${ssc}
    [Return]  ${None}

Compare sanSystemCredentials
    [Documentation]  Compare 2 lists of sanSystemCredentials
    [Arguments]  ${sanStorageCredentials_1}  ${sanStorageCredentials_2}
    ${len1} =  Get Length  ${sanStorageCredentials_1}
    ${len2} =  Get Length  ${sanStorageCredentials_2}
    Should Be Equal  ${len1}  ${len2}
    :FOR  ${ssc1}  IN  @{sanStorageCredentials_1}
    \   ${ssc2} =  Get sanStorageCredential by URI  ${sanStorageCredentials_2}  ${ssc1['storageSystemUri']}
    \   Should Be Equal  ${ssc1['chapLevel']}  ${ssc2['chapLevel']}

Get Volume by ID
    [Documentation]  Given a list of volumeAttachments and an ID, return the matching element
    [Arguments]  ${volumeAttachments}  ${id}
    :FOR  ${va}  IN  @{volumeAttachments}
    \   Return From Keyword If  ${va['id']} == ${id}  ${va}
    [Return]  ${None}

SP Volume CHAP Settings is None
    [Documentation]  Verify sanSystemCredentials record for No Chap
    [Arguments]  ${sscred}  ${cliq_data}
    Should Be Equal  ${sscred['chapLevel']}  None
    Should Be Equal  ${cliq_data['PERMISSION']['chapRequired']}  false

SP Volume CHAP Setting is CHAP
    [Documentation]  Verify sanSystemCredentials record for Chap
    [Arguments]  ${sscred}  ${cliq_data}
    Should Be Equal  ${sscred['chapLevel']}  Chap
    Should Be Equal  ${cliq_data['PERMISSION']['chapRequired']}  true
    Should Be Empty  ${cliq_data['PERMISSION']['initiatorSecret']}
    Should Be Equal  ${cliq_data['PERMISSION']['targetSecret']}  ${sscred['chapSecret']}

SP Volume CHAP Setting is MutualChap
    [Documentation]  Verify sanSystemCredentials record for MutualChap
    [Arguments]  ${sscred}  ${cliq_data}
    Should Be Equal  ${sscred['chapLevel']}  MutualChap
    Should Be Equal  ${cliq_data['PERMISSION']['chapRequired']}  true
    Should Be Equal  ${cliq_data['PERMISSION']['initiatorSecret']}  ${sscred['mutualChapSecret']}
    Should Be Equal  ${cliq_data['PERMISSION']['targetSecret']}  ${sscred['chapSecret']}

SP Volume CHAP Setting Should Match Storage CHAP Setting
    [Documentation]  Verify a Serve Profile volume's CHAP settings and StoreVirtual CHAP settings for a given CHAP level
    [Arguments]  ${sanStorage}  ${vol_id}  ${cliq_credentials}  ${chap_level}
    ${vol_attachment}=  Get Volume by ID  ${sanStorage['volumeAttachments']}  ${vol_id}
    ${vol}=  Get Resource  ${vol_attachment['volumeUri']}
    ${sscred}=  Get sanStorageCredential by URI  ${sanStorage['sanSystemCredentials']}  ${vol_attachment['volumeStorageSystemUri']}
    ${cliq_result}=  CLIQ Get Volume Info  ${vol['deviceVolumeName']}  False  ${cliq_credentials}
    ${cliq_data}=  VsaHelper.parse_cliq_volume_info  ${cliq_result}
    Should Be Equal  ${cliq_data['RESPONSE']['name']}  CliqSuccess
    Should Be Equal  ${cliq_data['VOLUME']['name']}  ${vol['deviceVolumeName']}
    Run Keyword and Return If  '${chap_level}' == 'None'  SP Volume CHAP Settings is None  ${sscred}  ${cliq_data}
    Run Keyword and Return If  '${chap_level}' == 'Chap'  SP Volume CHAP Setting is CHAP  ${sscred}  ${cliq_data}
    Run Keyword and Return If  '${chap_level}' == 'MutualChap'  SP Volume CHAP Setting is MutualChap  ${sscred}  ${cliq_data}
    Fail  Internal error - unrecognized CHAP level

SP Volumes CHAP Settings Should Match Storage CHAP Settings
    [Documentation]  Verify complete set of Server Profile volumes' CHAP settings and StoreVirtual CHAP settings
    [Arguments]  ${sp_name}  ${chap1}  ${chap2}=${None}
    ${sp}=  Get Resource  SP:${sp_name}
    SP Volume CHAP Setting Should Match Storage CHAP Setting  ${sp['sanStorage']}  1  ${cliq_credentials_sv1}  ${chap1}
    SP Volume CHAP Setting Should Match Storage CHAP Setting  ${sp['sanStorage']}  2  ${cliq_credentials_sv1}  ${chap1}
    Run Keyword If  '${chap2}' != '${None}'  SP Volume CHAP Setting Should Match Storage CHAP Setting  ${sp['sanStorage']}  3  ${cliq_credentials_sv2}  ${chap2}

SP Compliance is
    [Documentation]  Verify that the SP is in compliance with its SPT
    [Arguments]  ${sp_name}  ${compliance_level}
    # attempt to let async compliance check complete, is there a better way to do this?
    Sleep  10s
    ${sp}=  Get Resource  SP:${sp_name}
    Should Be Equal  ${sp['templateCompliance']}  ${compliance_level}

SP Compliance is Compliant
    [Documentation]  Verify that the SP is in compliance with its SPT
    [Arguments]  ${sp_name}
    SP Compliance is  ${sp_name}  Compliant

SP Compliance is NonCompliant
    [Documentation]  Verify that the SP is not in compliance with its SPT
    [Arguments]  ${sp_name}
    SP Compliance is  ${sp_name}  NonCompliant

SP Compliance is Unknown
    [Documentation]  Verify that the SP compliance is unknown, usually due to not being derived from an SPT
    [Arguments]  ${sp_name}
    SP Compliance is  ${sp_name}  Unknown

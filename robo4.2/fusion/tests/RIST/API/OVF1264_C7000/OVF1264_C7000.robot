*** Settings ***
Documentation                   OVF1264 - SD Card Boot Support for C7000

Library             FusionLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             Dialogs
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords     Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Remove all Profiles and Templates    ${ts0_create_profiles}
Suite Teardown      Run Keywords    Remove all Profiles and Templates    ${ts0_create_profiles}
...                 AND     Remove All DL Server Hardware Async
...                 AND     Fusion Api Logout Appliance

*** Variables ***

*** Test Cases ***
OVF1264 C7000 TS0 - Create Server Profile with SD Boot
    [Tags]    C7000_TS0_SP_SDBoot
    Power Off Servers in Profiles    ${ts0_create_profiles}
    ${resp_list} =    Add Server Profiles from variable    ${ts0_create_profiles}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    :FOR    ${profile}    IN    @{ts0_create_profiles}
    \    Verify Server Profile    ${profile}    status=OK

OVF1264 C7000 TS0 - Verify Pending Server Settings with RIS After Create
    [Tags]     C7000_TS0_Verify
    Verify RIS nodes for list    ${ts0_ris_after_create_pending}    DISABLE_LIST_SORTING=${False}

OVF1264 C7000 TS0 - Power on Servers After Create and Boot to POST
    [Tags]    C7000_TS0_Power_POST
    Power on Servers in Profiles    ${ts0_create_profiles}
    Wait for Servers in Profiles to reach POST State    ${ts0_create_profiles}    post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST    timeout=15m    interval=10s

OVF1264 C7000 TS0 - Verify Server Settings with RIS After Create
    [Tags]     C7000_TS0_Verify_POST
    Verify RIS nodes for list    ${ts0_ris_after_create}    DISABLE_LIST_SORTING=${False}

OVF1264 C7000 TS1 - Edit Server Profile Remove SD Boot
    [Tags]    C7000_TS1_Edit1
    Power Off Servers in Profiles    ${ts1_edit_profiles1}
    ${resp_list} =    Edit Server Profiles from variable    ${ts1_edit_profiles1}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    :FOR    ${profile}    IN    @{ts1_edit_profiles1}
    \     Verify Server Profile    ${profile}    status=OK

OVF1264 C7000 TS1 - Verify Pending Server Settings with RIS After First Edit
    [Tags]    C7000_TS1_Verify_Edit1
    Verify RIS nodes for list    ${ts1_ris_after_edit1_pending}    DISABLE_LIST_SORTING=${False}

OVF1264 C7000 TS1 - Power on Servers After First Edit and Boot to POST
    [Tags]    C7000_TS1_Power_Edit1
    Power on Servers in Profiles    ${ts1_edit_profiles1}
    Wait for Servers in Profiles to reach POST State    ${ts1_edit_profiles1}    post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST    timeout= 5m    interval= 0s

OVF1264 C7000 TS1 - Verify Server Settings with RIS After Edit to Remove SD Boot
    [Tags]  C7000_TS1_Verify_Edit1_POST
    Verify RIS nodes for list    ${ts1_ris_after_edit1}    DISABLE_LIST_SORTING=${True}

OVF1264 C7000 TS1 - Edit Server Profile and Add SD Boot
    [Tags]    C7000_TS1_Edit2
    Power Off Servers in Profiles    ${ts1_edit_profiles2}
    ${resp_list} =    Edit Server Profiles from variable    ${ts1_edit_profiles2}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    :FOR  ${profile}  IN  @{ts1_edit_profiles2}
    \     Verify Server Profile    ${profile}    status=OK

OVF1264 C7000 TS1 - Verify Pending Server Settings with RIS After Second Edit to Add SD Boot
    [Tags]    C7000_TS1_Verify_Edit2
    # can use ${ts0_ris_after_create_pending} as SD Card is now Boot Device
    Verify RIS nodes for list    ${ts0_ris_after_create_pending}    DISABLE_LIST_SORTING=${True}

OVF1264 C7000 TS1 - Power on Servers After Second Edit and Boot to POST
    [Tags]    C7000_TS1_Power_POST
    Power on Servers in Profiles    ${ts1_edit_profiles2}
    Wait for Servers in Profiles to reach POST State    ${ts1_edit_profiles2}    post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST    timeout=15m    interval=10s

OVF1264 C7000 TS1 - Verify Server Settings with RIS After Edit to Add SD Boot
    [Tags]    C7000_TS1_Verify_Edit2_POST
    # can use ${ts0_ris_after_create} as SD Card now Boo Device
    Verify RIS nodes for list    ${ts0_ris_after_create}    DISABLE_LIST_SORTING=${False}

OVF1264 C7000 TS2 - Move Server Profile with SD Boot
    [Tags]    C7000_TS2_Move_SDBoot
    [Setup]  Delete Server Profiles  ${ts2_delete_profiles_before_move}
    Power Off Servers in Profiles    ${ts1_edit_profiles2}
    Power Off Servers in Profiles    ${ts2_move_profiles}
    ${resp_list} =    Edit Server Profiles from variable    ${ts2_move_profiles}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    :FOR    ${profile}    IN    @{ts2_move_profiles}
    \    Verify Server Profile    ${profile}    status=OK

OVF1264 C7000 TS2 - Verify Pending Server Settings with RIS After Move to Remove SD Boot
    [Tags]    C7000_TS2_Verify_After_Move
    Verify RIS nodes for list    ${ts2_ris_after_move}    DISABLE_LIST_SORTING=${True}

OVF1264 C7000 TS2 - Power on Servers After Move and Boot to POST
    [Tags]    C7000_TS2_Power_POST_Move
    Power on Servers in Profiles    ${ts2_move_profiles}
    Wait for Servers in Profiles to reach POST State    ${ts2_move_profiles}    post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST    timeout=15m    interval=10s

OVF1264 C7000 TS2 - Verify Server Settings with RIS After Move
    [Tags]    C7000_TS2_Verify_Move_POST
    Verify RIS nodes for list    ${ts2_ris_after_move}    DISABLE_LIST_SORTING=${False}
    [Teardown]    Delete Server Profiles    ${ts2_clean_up}

OVF1264 C7000 TS3 - Create Server Profile Template with SD Boot
    [Tags]    C7000_TS3_SPT_SDBoot
    ${resp_list} =    Add Server Profile Templates from variable    ${ts3_create_templates}
    Wait For Task2    ${resp_list}    timeout=60    interval=10
    Verify Server Profile Templates    ${ts3_create_templates}    status=OK

OVF1264 C7000 TS4 - Edit Server Profile Template with SD Boot
    [Tags]    C7000_TS4_Edit_SPT
    ${resp_list} =    Edit Server Profile Templates from variable    ${ts4_edit_templates}
    Wait For Task2    ${resp_list}    timeout=60    interval=10
    Verify Server Profile Templates    ${ts4_edit_templates}    status=OK
    [Teardown]  Delete Templates  ${ts4_edit_templates}

OVF1264 C7000 TS5 - Create Server Profile from Template with SD Boot
    [Tags]    C7000_TS5_SP_From_SPT
    [Setup]    Create Initial SPT's    ${ts5_create_templates}
    Power Off Servers in Profiles    ${ts5_create_sp_from_spt}
    ${resp_list} =    Add Server Profiles from variable    ${ts5_create_sp_from_spt}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    :FOR    ${profile}    IN    @{ts5_create_sp_from_spt}
    \    Verify Server Profile    ${profile}    status=OK
    :FOR    ${profile}    IN    @{sp_compliance}
    \     Verify Server Profile Compliance    ${profile}
    [Teardown]    Clean up Resources    ${ts5_create_sp_from_spt}    ${ts5_create_templates}

OVF1264 C7000 TS6 - Verify Non - Compliance after SP Create
    [Tags]    C7000_TS6_NonCompliance_SP
    [Setup]    Create Initial SPT's    ${ts5_create_templates}
    Power Off Servers in Profiles    ${ts5_create_sp_from_spt}
    ${resp_list} =    Add Server Profiles from variable    ${ts6_create_sp_from_spt}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    :FOR    ${profile}    IN    @{ts6_create_sp_from_spt}
    \     Verify Server Profile    ${profile}    status=Warning
    :FOR    ${profile}    IN    @{ts6_non_compliance}
    \     Verify Server Profile Compliance    ${profile}
    ${resp_list} =    Edit Server Profiles from variable    ${ts5_create_sp_from_spt}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    :FOR    ${profile}    IN    @{ts5_create_sp_from_spt}
    \     Verify Server Profile    ${profile}    status=OK
    :FOR    ${profile}    IN    @{sp_compliance}
    \     Verify Server Profile Compliance    ${profile}
    [Teardown]    Clean up Resources    ${ts5_create_sp_from_spt}    ${ts5_create_templates}

OVF1264 C7000 TS7 - Verify Non - Compliance after SPT Edit
    [Tags]    C7000_TS7_NonCompliance_SPT_Edit
    [Setup]    Create Compliant SP's from SPT's  ${ts5_create_templates}  ${ts5_create_sp_from_spt}  ${sp_compliance}
    ${resp_list} =    Edit Server Profile Templates from variable    ${ts7_edit_templates}
    Wait For Task2    ${resp_list}    timeout=60    interval=10
    Verify Server Profile Templates    ${ts7_edit_templates}    status=OK
    :FOR    ${profile}    IN    @{ts7_non_compliance}
    \     Verify Server Profile Compliance    ${profile}
    ${resp_list} =    Edit Server Profile Templates from variable  ${ts5_create_templates}
    Wait For Task2    ${resp_list}    timeout=3600    interval= 0
    Verify Server Profile Templates    ${ts5_create_templates}    status=OK
    :FOR    ${profile}    IN    @{sp_compliance}
    \     Verify Server Profile Compliance    ${profile}
    [Teardown]    Clean up Resources    ${ts5_create_sp_from_spt}    ${ts5_create_templates}

OVF1264 C7000 TS8 - Create Template from Server Profile
    [Tags]    C7000_TS8_SPT_From_SP
    [Setup]    Create Initial SP's  ${ts0_create_profiles}
    ${resp_list} =    Create Server Profile Template from Profile    ${create_profile_gen9}    ${create_profile_gen9['name']}
    Wait For Task2    ${resp_list}    timeout=30  interval=10
    ${resp_list} =    Create Server Profile Template from Profile    ${create_profile_gen10}    ${create_profile_gen10['name']}
    Wait For Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates    ${ts5_create_templates}    status=OK
    [Teardown]  Clean up Resources    ${ts0_create_profiles}    ${ts5_create_templates}

OVF1264 C7000 TS9 - Negative Create SP with Legacy BIOs boot Mode SD Card primary boot source
    [Documentation]    OVTC36908: OVF1264: Synergy - Creating Server Profile with SD Boot and Legacy BIOs Boot Mode Should Fail Validation
    [Tags]    C7000_TS9_SDBoot_Legacy    NEGATIVE
    Run Negative Tasks for List    ${OVTC36891_Neg_Add_LegBIOS_SD_Primary}

OVF1264 C7000 TS10 - Negative Edit SP to Legacy BIOs boot Mode SD Card primary boot source
    [Documentation]    OVTC36911:  OVF1264: Synergy - Editing Server Profile to SD Boot and Legacy BIOs Boot Mode Should Fail Validation
    [Tags]    C7000_TS10_Edit_SDBoot_Legacy    NEGATIVE
    ${resp_list} =    Add Server Profiles from variable    ${OVS27399_Add_LegBIOS_For_Neg_Edit}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    Run Negative Tasks for List    ${OVTC36893_Neg_Edit_LegBIOS_SD_Primary}

OVF1264 C7000 TS11 - Negative Editing Server Profile to Invalid Boot Device Should Fail Validation
    [Documentation]    OVTC36913: OVF1264: Synergy - Editing Server Profile to Invalid Boot Device Should Fail Validation
    [Tags]    C7000_TS11_Edit_Invalid_Boot    NEGATIVE
    # this edit sets to UEFI with SD boot so we can try to set to an invalid boot
    ${resp_list} =    Edit Server Profiles from variable    ${ts0_create_profiles}
    Wait For Task2  ${resp_list}    timeout=3600    interval=10
    Run Negative Tasks for List    ${OVTC36894_Neg_Edit_SDBoot_To_Invalid}

OVF1264 C7000 TS12 - Creating Server Profile with SD Boot on Unsupported Server Should Fail Validation
    [Documentation]    OVTC36909 OVF1264: C7000 - Creating Server Profile with SD Boot on Unsupported Server Should Fail Validation
    [Tags]    C7000_TS12_SP_SDBoot_Unsupported    NEGATIVE
    Run Negative Tasks for List    ${Neg_Add_SD_Primary}

OVF1264 C7000 TS13 - Editing Server Profile and Adding SD Boot on Unsupported Server Should Fail Validation
    [Documentation]    OVTC36912  OVF1264: C7000 - Editing Server Profile and Adding SD Boot on Unsupported Server Should Fail Validation
    [Tags]    C7000_TS13_Edit_SDBoot_Unsupported    NEGATIVE
    ${resp_list} =    Add Server Profiles from variable    ${Gen8_For_Neg}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    Run Negative Tasks for List    ${Neg_Edit_SD_Primary}
    ${resp_list} =    Remove Server Profiles from variable     ${Gen8_For_Neg}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10

OVF1264 C7000 TS14 - Moving a Server Profile with SD Boot to an Unsupported Server Should Fail Validation
    [Documentation]    OVTC36914  OVF1264: C7000 - Moving a Server Profile with SD Boot to an Unsupported Server Should Fail Validation
    [Tags]    C7000_TS14_Move_SDBoot_Unsupported    NEGATIVE
    Run Negative Tasks for List    ${Neg_move_Gen9SD_to_Gen8}

Add DL380 Gen10 server as managed
    [Documentation]    Add Gen10 DL servers as managed
    [Tags]    Add_DL_Server
    ${resps} =    Add Server hardware from variable    ${Gen10_DLs}
    Wait For Task2    ${resps}    timeout=10m    interval=5

OVF1264 DL TS15 - Creating Server Profile with SD Boot on Unsupported Server Should Fail Validation
    [Documentation]    OVTC36917  OVF1264: DL - Creating Server Profile with SD Boot on Unsupported Server Should Fail Validation
    [Tags]    DL_TS15_SP_SDBoot_Unsupported    NEGATIVE
    Run Negative Tasks for List    ${DL_Neg_Create_SP}

OVF1264 DL TS16 - Editing Server Profile and Adding SD Boot on Unsupported Server Should Fail Validation
    [Documentation]    OVTC36918  OVF1264: DL - Editing Server Profile and Adding SD Boot on Unsupported Server Should Fail Validation
    [Tags]    DL_TS16_Edit_SDBoot_Unsupported    NEGATIVE
    [Teardown]    Delete Server Profiles    ${DL_For_Neg}
    ${resp_list} =    Add Server Profiles from variable    ${DL_For_Neg}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    Run Negative Tasks for List    ${DL_Neg_Edit_SP}

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  set log level to TRACE, log the variaables & login to the appliance as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance    ${APPLIANCE_IP}    ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Remove all SP's and SPT"s
    [Arguments]    ${profiles}
    Power off ALL servers
    ${resplist} =    Remove Server Profiles by Server Hardware    ${profiles}
    Wait For Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5

Create Initial SPT's
    [Documentation]  Create SPT's for test case setup
    [Arguments]    ${profile_templates}
    ${resp_list} =    Add Server Profile Templates from variable    ${profile_templates}
    Wait For Task2    ${resp_list}    timeout=30    interval=10

Create Initial SP's
    [Documentation]  Create SP's for test case setup
    [Arguments]    ${profiles}
    ${resp_list} =    Add Server Profiles from variable    ${profiles}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10

Delete Server Profiles
    [Documentation]  Delete the passed in Server Profiles
    [Arguments]    ${server_profiles}
    Power Off Servers in Profiles    ${server_profiles}
    ${resp_list} =    Remove Server Profiles from variable    ${server_profiles}    force=${True}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10

Delete Templates
    [Documentation]  Delete the passed in Server Profile Templates
    [Arguments]    ${server_profile_templates}
    ${resp_list} =    Remove Server Profile Templates from variable    ${server_profile_templates}
    Wait For Task2    ${resp_list}    timeout=60    interval=10

Clean up Resources
    [Documentation]  Delete SP's & SPT's
    [Arguments]    ${profiles}    ${profile_templates}
    ${resp_list} =    Remove Server Profiles from variable    ${profiles}
    Wait For Task2    ${resp_list}    timeout=3600    interval=10
    ${resp_list} =    Remove Server Profile Templates from variable    ${profile_templates}
    Wait For Task2    ${resp_list}    timeout=60    interval=10

Create Compliant SP's from SPT's
    [Documentation]    Create compliant SP's from SPT's
    [Arguments]    ${profile_templates}    ${profiles}    ${compliance}
    ${resp_list} =    Add Server Profile Templates from variable    ${profile_templates}
    Wait For Task2  ${resp_list}    timeout=30    interval=10
    ${resp_list} =    Add Server Profiles from variable    ${profiles}
    Wait For Task2    ${resp_list}    timeout=1500    interval=10
    :FOR    ${profile}    IN    @{compliance}
    \     Verify Server Profile Compliance    ${profile}

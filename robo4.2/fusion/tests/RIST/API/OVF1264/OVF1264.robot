*** Settings ***
Documentation                   OVF1264 - SD Card Boot Support for Synergy

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
...                 AND     Fusion Api Logout Appliance

*** Variables ***

*** Test Cases ***
OVF1264 Synergy TS0 - Create Server Profile with SD Boot
    [Tags]    TS0_Create_SD_Boot
    Power Off Servers in Profiles  ${ts0_create_profiles}
    ${resp_list} =  Add Server Profiles from variable  ${ts0_create_profiles}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts0_create_profiles}
    \   Verify Server Profile  ${profile}  status=OK

OVF1264 Synergy TS0 - Verify Pending Server Settings with RIS After Create
    [Tags]    TS0_Verify
    Verify RIS nodes for list  ${ts0_ris_after_create}  DISABLE_LIST_SORTING=${False}

OVF1264 Synergy TS0 - Power on Servers After Create and Boot to POST
    [Tags]    TS0_Power_POST
    Power on Servers in Profiles  ${ts0_create_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts0_create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=20m  interval=10s

OVF1264 Synergy TS0 - Verify Server Settings with RIS After Create
    [Tags]    TS0_Verify_POST
    Verify RIS nodes for list  ${ts0_ris_after_create}  DISABLE_LIST_SORTING=${False}

OVF1264 Synergy TS1 - Edit Server Profile Remove SD Boot
    [Tags]    TS1_Edit1
    Power Off Servers in Profiles  ${ts1_edit_profiles1}
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_profiles1}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts1_edit_profiles1}
    \   Verify Server Profile  ${profile}  status=OK

OVF1264 Synergy TS1 - Verify Pending Server Settings with RIS After First Edit
    [Tags]    TS1_Verify_Edit1
    # Edit in "pending state" thus can verify with previous create data
    Verify RIS nodes for list  ${ts0_ris_after_create}  DISABLE_LIST_SORTING=${False}

OVF1264 Synergy TS1 - Power on Servers After First Edit and Boot to POST
    [Tags]    TS1_Power_POST_Edit1
    Power on Servers in Profiles  ${ts1_edit_profiles1}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF1264 Synergy TS1 - Verify Server Settings with RIS After Edit to Remove SD Boot
    [Tags]    TS1_Verify_Edit1_POST
    Verify RIS nodes for list  ${ts1_ris_after_edit1}  DISABLE_LIST_SORTING=${True}

OVF1264 Synergy TS1 - Edit Server Profile and Add SD Boot
    [Tags]   TS1_Edit_2
    Power Off Servers in Profiles  ${ts1_edit_profiles2}
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_profiles2}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts1_edit_profiles2}
    \   Verify Server Profile  ${profile}  status=OK

OVF1264 Synergy TS1 - Verify Pending Server Settings with RIS After Second Edit to Remove SD Boot
    [Tags]    TS1_Verify_Edit2
    # Edit in "pending satate" thus can verify with previous edit data
    Verify RIS nodes for list  ${ts1_ris_after_edit1}  DISABLE_LIST_SORTING=${True}

OVF1264 Synergy TS1 - Power on Servers After Second Edit and Boot to POST
    [Tags]    TS1_Power_POST_Edit2
    Power on Servers in Profiles  ${ts1_edit_profiles2}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF1264 Synergy TS1 - Verify Server Settings with RIS After Edit to Add SD Boot
    [Tags]    TS1_Verify_Edit2_POST
    # can use original ts0_ris_after_create data as SD boot now set again
    Verify RIS nodes for list  ${ts0_ris_after_create}  DISABLE_LIST_SORTING=${False}

OVF1264 Synergy TS2 - Move Server Profile with SD Boot
    [Tags]    TS2_Move_SDBoot
    [Setup]  Delete Server Profiles  ${ts2_delete_profiles_before_move}
    Power Off Servers in Profiles  ${ts1_edit_profiles2}
    Power Off Servers in Profiles  ${ts2_move_profiles}
    ${resp_list} =  Edit Server Profiles from variable  ${ts2_move_profiles}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts2_move_profiles}
    \   Verify Server Profile  ${profile}  status=OK

OVF1264 Synergy TS2 - Verify Pending Server Settings with RIS After Move to Remove SD Boot
    [Tags]    TS2_Verify_After_Move
    Verify RIS nodes for list  ${ts2_ris_after_move}  DISABLE_LIST_SORTING=${True}

OVF1264 Synergy TS2 - Power on Servers After Move and Boot to POST
    [Tags]    TS2_Power_POST_Move
    Power on Servers in Profiles  ${ts2_move_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts2_move_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF1264 Synergy TS2 - Verify Server Settings with RIS After Move
    [Tags]    TS2_Verify_Move_POST
    Verify RIS nodes for list  ${ts2_ris_after_move}  DISABLE_LIST_SORTING=${False}
    [Teardown]  Delete Server Profiles  ${ts2_clean_up}

OVF1264 Synergy TS3 - Create Server Profile Template with SD Boot
    [Tags]    TS3_SPT_SDBoot
    ${resp_list} =  Add Server Profile Templates from variable  ${ts3_create_templates}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts3_create_templates}  status=OK

OVF1264 Synergy TS4 - Edit Server Profile Template with SD Boot
    [Tags]    TS4_Edit_SPT
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts4_edit_templates}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts4_edit_templates}  status=OK
    [Teardown]  Delete Templates  ${ts4_edit_templates}

OVF1264 Synergy TS5 - Create Server Profile from Template with SD Boot
    [Tags]    TS5_SP_From_SPT
    [Setup]  Create Initial SPT's  ${ts5_create_templates}
    Power Off Servers in Profiles  ${ts5_create_sp_from_spt}
    ${resp_list} =  Add Server Profiles from variable  ${ts5_create_sp_from_spt}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts5_create_sp_from_spt}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}
    [Teardown]  Clean up Resources  ${ts5_create_sp_from_spt}  ${ts5_create_templates}

OVF1264 Synergy TS6 - Verify Non-Compliance after SP Create
    [Tags]    TS6_NonCompliance_SP
    [Setup]  Create Initial SPT's  ${ts5_create_templates}
    Power Off Servers in Profiles  ${ts5_create_sp_from_spt}
    ${resp_list} =  Add Server Profiles from variable  ${ts6_create_sp_from_spt}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts6_create_sp_from_spt}
    \   Verify Server Profile  ${profile}  status=Warning
    :FOR  ${profile}  IN  @{ts6_non_compliance}
    \   Verify Server Profile Compliance  ${profile}
    ${resp_list} =  Edit Server Profiles from variable  ${ts5_create_sp_from_spt}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts5_create_sp_from_spt}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}
    [Teardown]  Clean up Resources  ${ts5_create_sp_from_spt}  ${ts5_create_templates}

OVF1264 Synergy TS7 - Verify Non-Compliance after SPT Edit
    [Tags]    TS7_NonCompliace_SPT_Edit
    [Setup]  Create Compliant SP's from SPT's  ${ts5_create_templates}  ${ts5_create_sp_from_spt}  ${sp_compliance}
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts7_edit_templates}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts7_edit_templates}  status=OK
    :FOR  ${profile}  IN  @{ts7_non_compliance}
    \   Verify Server Profile Compliance  ${profile}
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts5_create_templates}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    Verify Server Profile Templates  ${ts5_create_templates}  status=OK
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}
    [Teardown]  Clean up Resources  ${ts5_create_sp_from_spt}  ${ts5_create_templates}

OVF1264 Synergy TS8 - Create Template from Server Profile
    [Tags]    TS8_SPT_From_SP
    [Setup]  Create Initial SP's  ${ts0_create_profiles}
    ${resp_list}=  Create Server Profile Template from Profile  ${create_profile_gen9}  ${create_profile_gen9['name']}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    ${resp_list}=  Create Server Profile Template from Profile  ${create_profile_gen10}  ${create_profile_gen10['name']}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts5_create_templates}  status=OK
    [Teardown]  Clean up Resources  ${ts0_create_profiles}  ${ts5_create_templates}

OVF1264 Synergy TS9 - Negative Create SP with Legacy BIOs boot Mode SD Card primary boot source
    [Documentation]    OVTC36891: OVF1264: Synergy - Creating Server Profile with SD Boot and Legacy BIOs Boot Mode Should Fail Validation
    [Tags]    TS9_SDBoot_Legacy   NEGATIVE
    Run Negative Tasks for List    ${OVTC36891_Neg_Add_LegBIOS_SD_Primary}

OVF1264 Synergy TS10 - Negative Edit SP to Legacy BIOs boot Mode SD Card primary boot source
    [Documentation]    OVTC36893: OVF1264: Synergy - Editing Server Profile to SD Boot and Legacy BIOs Boot Mode Should Fail Validation
    [Tags]    TS10_Edit_SDBoot_Legacy    NEGATIVE
    ${resp_list} =    Add Server Profiles from variable    ${OVS27399_Add_LegBIOS_For_Neg_Edit}
    Wait for Task2    ${resp_list}    timeout=3600    interval=10
    Run Negative Tasks for List    ${OVTC36893_Neg_Edit_LegBIOS_SD_Primary}

OVF1264 Synergy TS11 - Negative Editing Server Profile to Invalid Boot Device Should Fail Validation
    [Documentation]    OVTC36894: OVF1264: Synergy - Editing Server Profile to Invalid Boot Device Should Fail Validation
    [Tags]    TS11_Edit_Invalid_Boot   NEGATIVE
    # this edit sets to UEFI with SD boot so we can try to set to an invalid boot
    ${resp_list} =  Edit Server Profiles from variable  ${ts0_create_profiles}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    Run Negative Tasks for List    ${OVTC36894_Neg_Edit_SDBoot_To_Invalid}

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  set log level to TRACE, log the variaables & login to the appliance as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Remove all SP's and SPT"s
    [Arguments]    ${profiles}
    Power off ALL servers
    ${resplist} =    Remove Server Profiles by Server Hardware    ${profiles}
    Wait for Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait for Task2    ${sptlist}    timeout=600    interval=5

Create Initial SPT's
    [Documentation]  Create SPT's for test case setup
    [Arguments]  ${profile_templates}
    ${resp_list}=  Add Server Profile Templates from variable  ${profile_templates}
    Wait for Task2  ${resp_list}  timeout=30  interval=10

Create Initial SP's
    [Documentation]  Create SP's for test case setup
    [Arguments]  ${profiles}
    ${resp_list}=  Add Server Profiles from variable  ${profiles}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10

Delete Server Profiles
    [Documentation]  Delete the passed in Server Profiles
    [Arguments]  ${server_profiles}
    Power Off Servers in Profiles  ${server_profiles}
    ${resp_list}=  Remove Server Profiles from variable	 ${server_profiles}  force=${True}
    wait for task2  ${resp_list}  timeout=3600  interval=10

Delete Templates
    [Documentation]  Delete the passed in Server Profile Templates
    [Arguments]  ${server_profile_templates}
    ${resp_list}=  Remove Server Profile Templates from variable  ${server_profile_templates}
    wait for task2  ${resp_list}  timeout=60  interval=10

Clean up Resources
    [Documentation]  Delete SP's & SPT's
    [Arguments]  ${profiles}  ${profile_templates}
    ${resp_list}=  Remove Server Profiles from variable	 ${profiles}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    ${resp_list}=  Remove Server Profile Templates from variable	 ${profile_templates}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

Create Compliant SP's from SPT's
    [Documentation]  Create compliant SP's from SPT's
    [Arguments]  ${profile_templates}  ${profiles}  ${compliance}
    ${resp_list}=  Add Server Profile Templates from variable  ${profile_templates}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    ${resp_list}=  Add Server Profiles from variable  ${profiles}
    Wait for Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{compliance}
    \   Verify Server Profile Compliance  ${profile}

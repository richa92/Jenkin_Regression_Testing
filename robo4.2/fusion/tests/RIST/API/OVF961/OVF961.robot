*** Settings ***
Documentation                   OVF959 [CGW] Server profile backend: Conversion to use volume properties "blob" when creating new volumes

Library             FusionLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             Dialogs
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords     Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Remove all Profiles and Templates
...                 AND     Add Existing Storage Volumes Async  ${existing_volumes}
...                 AND     Add Storage Volume Templates Async  ${create_volume_templates}
Suite Teardown      Run Keywords    Remove New Storage Volumes
...                 AND     Remove Existing Storage Volumes
...                 AND     Remove ALL Storage Volume Templates Async
...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${X_API_VERSION}     600

*** Test Cases ***
OVF961 TS0 - Create Server Profile Templates with Managed Storage (v600 API)
    [Tags]  TS0  CGW  SPT
    ${resp_list}=  Add Server Profile Templates from variable  ${ts0_create_spt}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts0_create_spt}  status=OK
    Verify Server Profile Templates  ${ts1_create_spt}  status=OK  api=500

OVF961 TS0 - Edit Server Profile Templates with Managed Storage (v600 API)
    [Tags]  TS0  CGW  SPT
    ${resp_list}=  Edit Server Profile Templates from variable  ${ts0_edit_spt}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts0_edit_spt}  status=OK
    Verify Server Profile Templates  ${ts1_edit_spt}  status=OK  api=500

OVF961 TS0 - Delete Created Resources
    [Tags]  TS0  SPT
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts0_edit_spt}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF961 TS1 - Create Server Profile Templates with Managed Storage (v500 API)
    [Tags]  TS1  LEGACY  SPT
    ${resp_list} =  Add Server Profile Templates from variable  ${ts1_create_spt}  api=500
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts1_verify_create_spt_v600}  status=OK
    Verify Server Profile Templates  ${ts1_create_spt}  status=OK  api=500

OVF961 TS1 - Edit Server Profile Templates with Managed Storage (v500 API)
    [Tags]  TS1  LEGACY  SPT
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts1_edit_spt}  api=500
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts1_verify_edit_spt_v600}  status=OK
    Verify Server Profile Templates  ${ts1_edit_spt}  status=OK  api=500

OVF961 TS1 - Delete Created Resources
    [Tags]  TS1  SPT
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts1_edit_spt}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF961 TS2 - Create Server Profile Templates with Managed Storage (v600 API)
    [Tags]  TS2  CGW  SPT
    ${resp_list}=  Add Server Profile Templates from variable  ${ts0_create_spt}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts0_create_spt}  status=OK
    Verify Server Profile Templates  ${ts1_create_spt}  status=OK  api=500

OVF961 TS2 - Edit Server Profile Templates with Managed Storage (v500 API)
    [Tags]  TS2  LEGACY  SPT
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts1_edit_spt}  api=500
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts2_verify_edit_spt_v600}  status=OK
    Verify Server Profile Templates  ${ts1_edit_spt}  status=OK  api=500

OVF961 TS2 - Delete Created Resources
    [Tags]  TS2  SPT
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts1_edit_spt}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF961 TS3 - Create Server Profile Templates with Managed Storage (v500 API)
    [Tags]  TS3  LEGACY  SPT
    ${resp_list} =  Add Server Profile Templates from variable  ${ts1_create_spt}  api=500
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts1_verify_create_spt_v600}  status=OK
    Verify Server Profile Templates  ${ts1_create_spt}  status=OK  api=500

OVF961 TS3 - Edit Server Profile Templates with Managed Storage (v600 API)
    [Tags]  TS3  CGW  SPT
    ${resp_list}=  Edit Server Profile Templates from variable  ${ts0_edit_spt}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Verify Server Profile Templates  ${ts0_edit_spt}  status=OK
    Verify Server Profile Templates  ${ts1_edit_spt}  status=OK  api=500

OVF961 TS3 - Delete Created Resources
    [Tags]  TS3  SPT
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts0_edit_spt}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF961 TS4 - Negative Create Server Profile Template Validation Tests
    [Tags]  TS4  NEGATIVE  SPT
    Run Negative Tasks for List  ${negative_create_profile_template_tasks}
    [Teardown]  Remove SPT's  ${ts4_all_templates}

OVF961 TS5 - Negative Edit Server Profile Template Validation Tests
    [Tags]  TS5  NEGATIVE  SPT
    [Setup]  Create Initial SPT's  ${create_negative_edit_profile_templates}
    Run Negative Tasks for List  ${negative_edit_profile_template_tasks}
    [Teardown]  Remove SPT's  ${remove_negative_edit_profile_template}

OVF961 TS6 - Create SP from SPT (v600 API)
    [Tags]  TS6  CGW  SP-from-SPT
    [Setup]  Create Initial SPT's  ${ts6_create_spt}
    ${resp_list}=  Add Server Profiles from variable  ${ts6_create_sp_from_spt_v600}
    Wait for Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{ts6_verify_sp_from_spt_v600}
    \   Verify Server Profile  ${profile}  status=OK
    Storage Volumes Should Match Expected DTOs  ${ts6_verify_volumes}
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}
    [Teardown]  Clean up Resources  ${ts6_create_sp_from_spt_v600}  ${ts6_delete_new_volumes}  ${ts6_create_spt}

OVF961 TS7 - Create SP from SPT (v500 API)
    [Tags]  TS7  LEGACY  SP-from-SPT
    [Setup]  Create Initial SPT's  ${ts7_create_spt}
    ${resp_list}=  Add Server Profiles from variable  ${ts7_create_sp_from_spt_v500}  api=500
    Wait for Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{ts7_verify_sp_from_spt_v500}
    \   Verify Server Profile  ${profile}  api=500  status=OK
    Storage Volumes Should Match Expected DTOs  ${ts7_verify_volumes}
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}
    [Teardown]  Clean up Resources  ${ts7_create_sp_from_spt_v500}  ${ts6_delete_new_volumes}  ${ts7_create_spt}

OVF961 TS8 - Verify Non-Compliance after SP Create
    [Tags]  TS8  CGW  SP-from-SPT  COMPLIANCE
    [Setup]  Create Initial SPT's  ${ts6_create_spt}
    ${resp_list}=  Add Server Profiles from variable  ${ts8_create_sp_non_compliant}
    Wait for Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{sp_non_compliant}
    \   Verify Server Profile Compliance  ${profile}
    [Teardown]  Clean up Resources  ${ts8_create_sp_non_compliant}  ${ts8_delete_new_volumes}  ${ts6_create_spt}

OVF961 TS9 - Verify Non-Compliance after SPT Edit
    [Tags]  TS9  CGW  SP-from-SPT  COMPLIANCE
    [Setup]  Create Compliant SP's from SPT's  ${ts6_create_spt}  ${ts6_create_sp_from_spt_v600}  ${sp_compliance}
    ${resp_list}=  Edit Server Profile Templates from variable  ${ts9_edit_spt_non_compliant}
    Wait for Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{spt_non_compliant}
    \   Verify Server Profile Compliance  ${profile}
    ${resp_list}=  Edit Server Profile Templates from variable  ${ts9_edit_spt_compliant}
    Wait for Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}
    [Teardown]  Clean up Resources  ${ts6_create_sp_from_spt_v600}  ${ts6_delete_new_volumes}  ${ts6_create_spt}

OVF961 TS10 - Verify Non-Compliance after VT Edit
    [Tags]  TS10  CGW  SP-from-SPT  COMPLIANCE
    [Setup]  Create Compliant SP's from SPT's  ${ts6_create_spt}  ${ts6_create_sp_from_spt_v600}  ${sp_compliance}
    # Edit All VT's and
    ${resplist} =  Edit Storage Volume Templates  ${ts10_edit_volume_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    sleep  5s
    Verify SPT Volume Template Alerts  ${ts10_expected_spt_alerts}
    Verify SP Volume Template Alerts  ${ts10_expected_sp_alerts}
    Verify Server Profile Templates  ${ts10_verify_spt_warning}  status=Warning
    :FOR  ${profile}  IN  @{ts10_verify_sp_warning}
    \   Verify Server Profile  ${profile}  status=Warning
    # Edit Profile1 volume 1 VT, verify alerts and Warning state persistists
    ${resplist} =  Edit Storage Volume Templates  ${ts10_edit2_volume_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    sleep  5s
    Verify SPT Volume Template Alerts  ${ts10_expected_spt_alerts2}
    Verify SP Volume Template Alerts  ${ts10_expected_sp_alerts2}
    Verify Server Profile Templates  ${ts10_verify_spt_warning}  status=Warning
    :FOR  ${profile}  IN  @{ts10_verify_sp_warning}
    \   Verify Server Profile  ${profile}  status=Warning
    # Edit All VT's back into compliance, verify alerts are cleared and OK state returned
    ${resplist} =  Edit Storage Volume Templates  ${ts10_edit3_volume_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    sleep  5s
    Verify SPT Volume Template Alerts  ${ts10_expected_alerts_cleared}
    Verify SP Volume Template Alerts  ${ts10_expected_alerts_cleared}
    Verify Server Profile Templates  ${ts10_verify_spt_warning}  status=OK
    :FOR  ${profile}  IN  @{ts10_verify_sp_warning}
    \   Verify Server Profile  ${profile}  status=OK
    [Teardown]  Clean up Resources  ${ts6_create_sp_from_spt_v600}  ${ts6_delete_new_volumes}  ${ts6_create_spt}

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  set log level to TRACE, log the variaables & login to the appliance as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Remove all SP's and SPT"s
    Power off ALL servers
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait for Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait for Task2    ${sptlist}    timeout=600    interval=5

Create Initial SPT's
    [Documentation]  Create SPT's for test case setup of TS6 & TS7
    [Arguments]  ${profile_templates}
    ${resp_list}=  Add Server Profile Templates from variable  ${profile_templates}
    Wait for Task2  ${resp_list}  timeout=30  interval=10

Create Compliant SP's from SPT's
    [Documentation]  Create compliant SP's from SPT's
    [Arguments]  ${profile_templates}  ${profiles}  ${compliance}
    ${resp_list}=  Add Server Profile Templates from variable  ${profile_templates}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    ${resp_list}=  Add Server Profiles from variable  ${profiles}
    Wait for Task2  ${resp_list}  timeout=1500  interval=10
    :FOR  ${profile}  IN  @{compliance}
    \   Verify Server Profile Compliance  ${profile}

Clean up Resources
    [Documentation]  Delete SP's, Volumes & SPT's
    [Arguments]  ${profiles}  ${volumes}  ${profile_templates}
    ${resp_list}=  Remove Server Profiles from variable	 ${profiles}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    ${resp_list} =  Remove Storage Volumes Async  ${volumes}  param=?suppressDeviceUpdates=false
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    ${resp_list}=  Remove Server Profile Templates from variable	 ${profile_templates}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

Remove SPT's
    [Documentation]  Delete SPT's
    [Arguments]  ${profile_templates}
    ${resp_list}=  Remove Server Profile Templates from variable  ${profile_templates}
    Run Keyword and Ignore Error  Wait for Task2  ${resp_list}  timeout=60  interval=10

Remove Server Profiles after Negative Validation Tasks
    [Documentation]  Remove all SP's that could potentailly be created from "OVF961 TS4 - Negative Create Server Profile Validation Tests"
    ${resp_list}=  Remove Server Profile Templates from variable  ${ts4_all_profiles}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

Verify SPT Volume Template Alerts
    [Documentation]  Verify VT Alerts are Present for SPT's
    [Arguments]  ${expected_alerts}
    ${spt_alerts} =  Get All Alerts by Param  param=?start=0&count=-1&filter="alertState EQ 'Active'"&filter=description like 'The following volume attachments are inconsistent with their volume template or invalid*'
    ${validate_status} =  Fusion api validate response follow  ${expected_alerts}  ${spt_alerts}  wordy=${False}
    Run Keyword If  '${validate_status}'=='False'  Fail  Failed to verify SPT Alerts

Verify SP Volume Template Alerts
    [Documentation]  Verify VT Alerts are Present for SP's
    [Arguments]  ${expected_alerts}
    ${sp_alerts} =  Get All Alerts by Param  param=?start=0&count=-1&filter="alertState EQ 'Active'"&filter=description like 'Volume * is inconsistent with its volume template, *'
    ${validate_status} =  Fusion api validate response follow  ${expected_alerts}  ${sp_alerts}  wordy=${False}
    Run Keyword If  '${validate_status}'=='False'  Fail  Failed to verify SP Alerts

Remove New Storage Volumes
    [Documentation]  Removes new storage volumes that were added during this test suite
    ${resplist} =  Remove Storage Volumes Async  ${all_new_volumes}  param=?suppressDeviceUpdates=false
     Wait for Task2  ${resp_list}  timeout=60  interval=10

Remove Existing Storage Volumes
    [Documentation]  Removes existing storage volumes that were added during the suite setup
    ${resplist} =  Remove Storage Volumes Async  ${existing_volumes}  param=?suppressDeviceUpdates=true
     Wait for Task2  ${resp_list}  timeout=60  interval=10

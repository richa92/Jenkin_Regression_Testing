*** Settings ***
Documentation                   OVF959 [CGW] Server profile backend: Conversion to use volume properties "blob" when creating new volumes

Library             FusionLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             Dialogs
Resource            ${CURDIR}\\..\\..\\..\\..\\\Resources\\api\\fusion_api_resource.txt
Variables           ${CURDIR}\\${DATA_FILE}

Suite Setup         Run Keywords     Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Remove all Profiles and Templates
...                 AND     Add Existing Storage Volumes Async  ${existing_volumes}
...                 AND     Add Storage Volume Templates Async  ${create_volume_templates}
Suite Teardown      Run Keywords    Remove all Profiles and Templates
...                 AND     Remove Storage Volumes Async  ${ts0_delete_new_volumes}  param=?suppressDeviceUpdates=false
...                 AND     Remove Storage Volumes Async  ${existing_volumes}  param=?suppressDeviceUpdates=true
...                 AND     Remove ALL Storage Volume Templates Async
...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${DATA_FILE}         wpst9_variables.py
#${X_API_VERSION}     600

*** Test Cases ***
TS0 - Create Server Profile with Managed Storage (v600 API)
    [Tags]  TS0
    ${resp_list}=  Add Server Profiles from variable  ${ts0_create_sp}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts0_verify_create_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts0_verify_create_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts0_verify_volumes_after_create}

TS0 - Edit Server Profile with Managed Storage (v600 API)
    [Tags]  TS0
    ${resp_list}=  Edit Server Profiles from variable  ${ts0_edit_sp}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts0_verify_edit_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts0_verify_edit_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts0_verify_volumes_after_edit}
    Storage Volumes Should Not Be Found  ${ts0_verify_nonpermanent_volumes_after_edit}

TS0 - Delete Created Resources
    [Tags]  TS0
    ${resp_list}=  Remove Server Profiles from variable	 ${ts0_edit_sp}  force=${True}
    wait for task2  ${resp_list}  timeout=60  interval=10
    Storage Volumes Should Not Be Found  ${ts0_verify_nonpermanent_volumes_after_delete}
    Storage Volumes Should Match Expected DTOs  ${ts0_verify_permanent_volumes_after_delete}
    Remove Storage Volumes Async  ${ts0_delete_new_volumes}  param=?suppressDeviceUpdates=false

TS1 - Create Server Profile with Managed Storage (v500 API)
    [Tags]  TS1
    ${resp_list} =  Add Server Profiles from variable  ${ts1_create_sp}  api=500  param=?force=true
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts1_verify_create_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts1_verify_create_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts1_verify_volumes_after_create}

TS1 - Edit Server Profile with Managed Storage (v500 API)
    [Tags]  TS1
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_sp}  api=500  param=?force=true
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts1_verify_edit_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts1_verify_edit_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts1_verify_volumes_after_edit}
    Storage Volumes Should Not Be Found  ${ts1_verify_nonpermanent_volumes_after_edit}

TS1 - Delete Created Resources
    [Tags]  TS1
    ${resp_list}=  Remove Server Profiles from variable	 ${ts1_edit_sp}  force=${True}
    wait for task2  ${resp_list}  timeout=60  interval=10
    Storage Volumes Should Not Be Found  ${ts1_verify_nonpermanent_volumes_after_delete}
    Storage Volumes Should Match Expected DTOs  ${ts1_verify_permanent_volumes_after_delete}
    Remove Storage Volumes Async  ${ts1_delete_new_volumes}  param=?suppressDeviceUpdates=false

TS2 - Create Server Profile with Managed Storage (v600 API)
    [Tags]  TS2
    ${resp_list}=  Add Server Profiles from variable  ${ts0_create_sp}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts0_verify_create_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts0_verify_create_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts2_verify_volumes_after_create}

TS2 - Edit Server Profile with Managed Storage (v500 API)
    [Tags]  TS2
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_sp}  api=500  param=?force=true
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts1_verify_edit_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts1_verify_edit_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts2_verify_volumes_after_edit}
    Storage Volumes Should Not Be Found  ${ts2_verify_nonpermanent_volumes_after_edit}

TS2 - Delete Created Resources
    [Tags]  TS2
    ${resp_list}=  Remove Server Profiles from variable	 ${ts1_edit_sp}  force=${True}
    wait for task2  ${resp_list}  timeout=60  interval=10
    Storage Volumes Should Not Be Found  ${ts2_verify_nonpermanent_volumes_after_delete}
    Storage Volumes Should Match Expected DTOs  ${ts2_verify_permanent_volumes_after_delete}
    Remove Storage Volumes Async  ${ts1_delete_new_volumes}  param=?suppressDeviceUpdates=false

TS3 - Create Server Profile with Managed Storage (v500 API)
    [Tags]  TS3
    ${resp_list} =  Add Server Profiles from variable  ${ts1_create_sp}  api=500  param=?force=true
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts1_verify_create_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts1_verify_create_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts3_verify_volumes_after_create}

TS3 - Edit Server Profile with Managed Storage (v600 API)
    [Tags]  TS3
    ${resp_list}=  Edit Server Profiles from variable  ${ts0_edit_sp}  param=?force=ignoreServerHealth,ignoreSANWarnings
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    :FOR  ${profile}  IN  @{ts0_verify_edit_sp_v600}
    \   Verify Server Profile  ${profile}  status=OK
    :FOR  ${profile}  IN  @{ts0_verify_edit_sp_v500}
    \   Verify Server Profile  ${profile}  status=OK  api=500
    Storage Volumes Should Match Expected DTOs  ${ts3_verify_volumes_after_edit}
    Storage Volumes Should Not Be Found  ${ts3_verify_nonpermanent_volumes_after_edit}

TS3 - Delete Created Resources
    [Tags]  TS3
    ${resp_list}=  Remove Server Profiles from variable	 ${ts0_edit_sp}  force=${True}
    wait for task2  ${resp_list}  timeout=60  interval=10
    Storage Volumes Should Not Be Found  ${ts3_verify_nonpermanent_volumes_after_delete}
    Storage Volumes Should Match Expected DTOs  ${ts3_verify_permanent_volumes_after_delete}
    Remove Storage Volumes Async  ${ts0_delete_new_volumes}  param=?suppressDeviceUpdates=false

TS4 - Negative Create Server Profile Validation Tests
    [Tags]  TS4  NEGATIVE
    Run Negative Tasks for List  ${negative_create_profile_tasks}

TS5 - Negative Edit Server Profile Validation Tests
    [Tags]  TS5  NEGATIVE
    ${resp_list}=  Add Server Profile  ${create_negative_edit_profile}
    Wait for Task2  ${resp_list}  timeout=30  interval=10
    Run Negative Tasks for List  ${negative_edit_profile_tasks}
    ${resp_list}=  Remove Server Profile	 ${create_negative_edit_profile}  force=${True}
    wait for task2  ${resp_list}  timeout=60  interval=10

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to trace, log the variables, and login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Power off all servers and remove all SP's and SPT's
    Power off ALL servers
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5
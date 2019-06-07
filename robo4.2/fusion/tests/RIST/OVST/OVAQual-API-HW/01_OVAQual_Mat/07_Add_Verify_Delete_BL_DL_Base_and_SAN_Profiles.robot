*** Settings ***
Documentation    Tests to verify profile creation with no storage volume,
...              with storage volume, create support dump and
...              delete profiles.
Resource                        ../resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure
*** Test Cases ***

Create Server Profiles Normal (no Storage Volumes)
    [Tags]    SETUP         SP
    [Documentation]     Create Server Profiles for BL and DL servers
    Power off Servers in Profiles  ${server_profiles_normal}
    ${responses}=  Add Server Profiles from variable  ${server_profiles_normal}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure   Wait For Task2  ${responses}
    ...  timeout=1500  interval=10
    Log All Warning and Critical Alerts
    Verify Resources for List  ${expected_server_profiles_normal}
    Get Task Tree From Post Response  ${responses}

Remove Server Profiles (no storage attached)
    [Tags]    TEARDOWN  REMOVE-SP
    [Documentation]  Remove Server Profiles for BL and DL servers
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure   Wait For Task2  ${responses}
    ...  timeout=900  interval=10
    Log All Warning and Critical Alerts
    Run Keyword If   ${responses} is not ${Null}   Verify Server profile exists

Create Server Profiles with Storage Volumes
    [Tags]    SPSV
    [Documentation]  Create Server Profiles for BL and DL servers with SAN Storage
    Power off Servers in Profiles  ${server_profile_with_storage}
    ${responses}=  Add Server Profiles from variable  ${server_profile_with_storage}
    Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure   Wait For Task2  ${responses}
    ...  timeout=2400  interval=10
    Log All Warning and Critical Alerts
    Verify Resources for List  ${expected_server_profile_with_storage}
    Get Task Tree From Post Response  ${responses}

Edit Server Profile Normal (no Change values)
   [Tags]    ESP
   [Documentation]    Edit server profile without any changes
   ${responses}=   Edit Server Profiles from variable   ${edit_server_profile_with_storage}
   Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure   Wait For Task2   ${responses}   timeout=1500    interval=10\
   Log All Warning and Critical Alerts
   Verify Resources for List  ${expected_edit_server_profile_with_storage}

Refresh Sever Profile
   [Tags]    RSP
   [Documentation]    Refresh server profile
   :FOR    ${profile}    IN    @{edit_server_profile_with_storage}
   \     ${responses}=   Patch Server Profile   ${profile}   op=replace    path=/refreshState   value=RefreshPending
   Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure     Wait For Task2   ${responses}   timeout=1500    interval=10\
   Log All Warning and Critical Alerts
   Verify Resources for List  ${expected_edit_server_profile_with_storage}

Update Server Profile Normal
   [Tags]    UPSP
   [Documentation]    Update server profiles
   Power off Servers in Profiles  ${update_server_profile_with_storage}
   ${responses}=   Edit Server Profiles from variable   ${update_server_profile_with_storage}
   Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure   Wait For Task2   ${responses}   timeout=1500    interval=10\
   Log All Warning and Critical Alerts
   Verify Resources for List  ${expected_update_server_profile_with_storage}

Get LE Support Dump
    [Tags]    LESD
    [Documentation]        Create and Download LE Support Dump
    Create And Download Logical Enclosure Support Dump  ${le_support_dump}  ${VERIFY}

Remove Server Profiles with storage attached
    [Tags]    TEARDOWN  REMOVE-SPSV
    [Documentation]  Remove Server Profiles for BL and DL servers with SAN Storage
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure   Wait For Task2  ${responses}
    ...  timeout=1200  interval=5
    Log All Warning and Critical Alerts
    Run Keyword If  ${responses} is not ${Null}  Verify Server profile exists
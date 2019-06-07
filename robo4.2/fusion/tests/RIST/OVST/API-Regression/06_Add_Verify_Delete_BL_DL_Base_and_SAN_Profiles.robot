*** Settings ***
Resource    resource.txt
Documentation    Create server profiles without storage volumes and with storage volumes

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
*** Test Cases ***

Create Server Profiles Normal (no Storage Volumes)
    [Tags]    SETUP         SP
    [Documentation]        Create Server Profiles for BL servers
    Power off Servers in Profiles   ${server_profiles}
    ${responses}=  Add Server Profiles from variable   ${server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1200    interval=5
    Verify Resources for List  ${expected_server_profiles}

Remove Server Profiles (no storage attached)
    [Tags]    TEARDOWN   REMOVE-SP
    [Documentation]     Remove Server Profiles for BL servers
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=5
    Run Keyword If   ${responses} is not ${Null}   Verify Server profile exists

Create Server Profiles with Storage Volumes
    [Tags]    SPSV
    [Documentation]        Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles   ${server_profile_with_storage}
    ${responses}=  Add Server Profiles from variable  ${server_profile_with_storage}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=2000    interval=5
    Verify Resources for List  ${expected_server_profile_with_storage}

Remove Server Profiles with storage attached
    [Tags]    TEARDOWN     REMOVE-SPSV
    [Documentation]        Remove Server Profiles for BL servers with SAN Storage
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=1200    interval=10
    Run Keyword If   ${responses} is not ${Null}   Verify Server profile exists
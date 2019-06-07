*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
Create Server Profiles without Storage Volumes
    [Tags]    SETUP  SP  TBIRD  C7000
    [Documentation]  Create Server Profiles for BL and DL servers
    Power off Servers in Profiles   ${server_profiles}
    ${responses}=    Add Server Profiles from variable   ${server_profiles}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2   ${responses}  timeout=1200  interval=5
    Verify Resources for List  ${expected_server_profiles}

Create Server Profiles with Storage Volumes
    [Tags]    SPSV   TBIRD  C7000
    [Documentation]  Create Server Profiles for BL and DL servers with SAN Storage
    Power off Servers in Profiles   ${server_profile_with_storage}
    ${responses}=    Add Server Profiles from variable  ${server_profile_with_storage}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2   ${responses}   timeout=2000  interval=5
    Verify Resources for List  ${expected_server_profile_with_storage}

*** Settings ***
Resource          ../resource.txt
Suite Setup       Fusion Api Login Appliance  ${appliance_ip}  ${credentials}
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
Add Server Profile Templates
    [Tags]     SPT   C7000  TBIRD
    [Documentation]  Add Server Profiles templates for servers
    ${responses}=    Add Non Existing Server Profile Templates  ${server_profile_templates}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}  timeout=600  interval=5
    Verify Resources for List  ${expected_server_profile_templates}

Create Server Profiles From Template
    [Tags]  SP-SPT   C7000  TBIRD
    [Documentation]  Add Server Profiles from Templates
    Power off Servers in Profiles   ${server_profiles_from_spt}
    ${responses}=    Create Non Existing Server Profile from SPT  ${server_profiles_from_spt}  ${VERIFY}
    Run Keyword If   ${responses} is not ${null}  Wait For Task2  ${responses}   timeout=600   interval=10
    Verify Resources for List  ${expected_server_profiles_from_spt}

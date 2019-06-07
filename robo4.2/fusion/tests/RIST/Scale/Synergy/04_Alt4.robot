*** Settings ***
Resource                        resource.txt
Suite Setup                     Scale Suite Setup     ${scaleuser_credentials}
Suite Teardown                  Scale Suite Teardown

*** Test Cases ***
Add Server Profile Templates
    [Tags]    SPT
    [Documentation]        Add Server Profiles templates for servers
    ${responses}=  Add Non Existing Server Profile Templates  ${server_profile_templates}
    Run Keyword for List with kwargs  ${responses}  Wait For Task2   timeout=600    interval=5
    Verify Scale Resources      ${server_profile_templates}

Create Server Profiles From Template
    [Tags]    SP-SPT
    [Documentation]        Add Server Profiles from Templates
    Power off Servers in Profiles   ${server_profiles}
    ${responses} =  Add Server Profiles from variable   ${server_profiles}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=600    interval=10
    Verify Scale Resources  ${expected_server_profiles_from_spt}


*** Settings ***
Resource        resource.txt
Suite Setup     Suite Setup Ping

# Setup\Teardown for ALL test cases
Test Setup      Scale Login     ${admin_credentials}
#Test Teardown   Scale Logout

*** Test Cases ***
Create Server Profiles From Template R5
    [Tags]    SPT4  SPT-ALL
    [Documentation]        Create Server Profiles From Template R5
    Power off Servers in Profiles   ${server_profiles_r4}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r4}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R6
    [Tags]    SPT7      SPT-ALL
    [Documentation]        Create Server Profiles From Template R6
    Power off Servers in Profiles   ${server_profiles_r7}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r7}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R8
    [Tags]    SPT8     SPT-ALL
    [Documentation]        Create Server Profiles From Template R8
    Power off Servers in Profiles   ${server_profiles_r8}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r8}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R9
    [Tags]    SPT9     SPT-ALL
    [Documentation]        Create Server Profiles From Template R9
    Power off Servers in Profiles   ${server_profiles_r9}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r9}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R10
    [Tags]    SPT10     SPT-ALL
    [Documentation]        Create Server Profiles From Template R10
    Power off Servers in Profiles   ${server_profiles_r10}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r10}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R15
    [Tags]    SPT15     SPT-ALL
    [Documentation]        Create Server Profiles From Template R15
    Power off Servers in Profiles   ${server_profiles_r15}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r15}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20


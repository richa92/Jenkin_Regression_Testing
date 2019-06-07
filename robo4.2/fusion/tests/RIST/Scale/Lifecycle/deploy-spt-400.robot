
*** Settings ***
Resource        resource.txt
Suite Setup     Suite Setup Ping     

# Setup\Teardown for ALL test cases
Test Setup      Scale Login     ${admin_credentials}
Test Teardown   Scale Logout

*** Test Cases ***
Create Server Profiles From Template R5
    [Tags]    SPT5  SPT-ALL
    [Documentation]        Create Server Profiles From Template R5
    Power off Servers in Profiles   ${server_profiles_r5}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r5}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R6
    [Tags]    SPT6      SPT-ALL
    [Documentation]        Create Server Profiles From Template R6
    Power off Servers in Profiles   ${server_profiles_r6}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r6}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R11
    [Tags]    SPT11     SPT-ALL
    [Documentation]        Create Server Profiles From Template R11
    Power off Servers in Profiles   ${server_profiles_r11}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r11}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R12
    [Tags]    SPT12     SPT-ALL
    [Documentation]        Create Server Profiles From Template R12
    Power off Servers in Profiles   ${server_profiles_r12}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r12}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R13
    [Tags]    SPT13     SPT-ALL
    [Documentation]        Create Server Profiles From Template R13
    Power off Servers in Profiles   ${server_profiles_r13}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r13}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R14
    [Tags]    SPT14     SPT-ALL
    [Documentation]        Create Server Profiles From Template R14
    Power off Servers in Profiles   ${server_profiles_r14}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r14}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

Create Server Profiles From Template R16
    [Tags]    SPT16     SPT-ALL
    [Documentation]        Create Server Profiles From Template R16
    Power off Servers in Profiles   ${server_profiles_r16}
    ${responses} =  Add Server Profiles from variable   ${server_profiles_r16}
    Run Keyword If  ${responses} is not ${null}     Wait For Task2   ${responses}   timeout=21500    interval=20

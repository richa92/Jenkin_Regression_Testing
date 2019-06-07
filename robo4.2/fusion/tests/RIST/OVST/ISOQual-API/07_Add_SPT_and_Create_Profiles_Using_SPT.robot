*** Settings ***
Documentation    Tests to verify profile creation with no storage volume,
...              with storage volume and create support dump.
...              delete profiles
Resource    resource.txt
Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown
Test Teardown                   Pause And Send EMail on Failure

*** Test Cases ***

Add Server Profile Templates
    [Tags]    SPT
    [Documentation]        Add Server Profiles templates for servers
    ${responses}=  Add Non Existing Server Profile Templates  ${server_profile_templates}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure     Wait For Task2   ${responses}   timeout=600    interval=5
    Verify Resources for List  ${expected_server_profile_templates}

Create Server Profiles From Template
    [Tags]    SP-SPT
    [Documentation]    Add Server Profiles from Templates
    Power off Servers in Profiles   ${server_profiles_from_spt}
    ${responses}=  Add Server Profiles from variable  ${server_profiles_from_spt}
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure     Wait For Task2   ${responses}   timeout=600    interval=10
    Log All Warning and Critical Alerts
    Verify Resources for List  ${expected_server_profiles_from_spt}
    Get Task Tree From Post Response  ${responses}

Edit Server Profile Templates
   [Tags]    ESPT
   [Documentation]    Edit server profile Templates with any changes
   ${responses}=   Edit Server Profile Templates from variable   ${edit_server_profile_templates}
   Run Keyword If  ${responses} is not ${null}   Run Keyword And Continue On Failure   Wait For Task2   ${responses}   timeout=1200    interval=5\
   Verify Resources for List  ${expected_edit_server_profile_templates}

Update Server Profile From SPT
   [Tags]    ESP-SPT
   [Documentation]    Update server profile from SPT
   ${response}     create list
   :FOR    ${profile}    IN    @{server_profiles_from_spt}
   \     ${resp}=   Patch Server Profile   ${profile}   op=replace    path=/templateCompliance   value=Compliant
   \     append to list  ${response}   ${resp}
   Run Keyword If  ${response} is not ${null}   Run Keyword And Continue On Failure     Wait For Task2   ${response}   timeout=1200    interval=5\
   Verify Resources for List  ${expected_edit_server_profiles_from_spt}
   
Remove Server Profiles
    [Tags]    REMOVE-SP-SPT
    [Documentation]        Remove Server Profiles
    ${responses}=  Remove All Server Profiles Async
    Run Keyword If  ${responses} is not ${null}    Run Keyword And Continue On Failure    Wait For Task2   ${responses}   timeout=600    interval=5
    Log All Warning and Critical Alerts
    Run Keyword If   ${responses} is not ${Null}    Verify Server profile exists

Remove Server Profile Templates
    [Tags]    REMOVE-SPT
    [Documentation]        Remove Server Profiles Templates for servers
    Remove All SPT
    Verify Server Profile Templates exist
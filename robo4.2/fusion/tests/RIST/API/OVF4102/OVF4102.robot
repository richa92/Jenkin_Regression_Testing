*** Settings ***
Documentation                   OVF4102 This feature is to enable adding/removing iLO administrator Password

Library        FusionLibrary
Library        BuiltIn
Library        Collections
Library        json
Library        Dialogs
Resource       ./../../../../Resources/api/fusion_api_resource.txt
Variables      ${DATA_FILE}

Suite Setup         OVF4102 - Setup
Suite Teardown      OVF4102 - Teardown

#Documentation        OVS29608 [OVF4102] As a Q2 tester define & write the SP & SPT  test cases for iLO Administrator password
Library              FusionLibrary


*** Test Cases ***
OVF4102 - Remove all Profiles and Templates
    [Documentation]  Clean up anything that may have been left around from ....
    Power off Servers in Profiles  ${create_sp}
    ${sptlist}  remove server profiles from variable  ${create_sp}
    Wait For Task2    ${sptlist}    timeout = 600    interval = 5
    ${resp_list}=  Remove Server Profile Templates from variable  ${create_spt}
    Run Keyword and Ignore Error  Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF4102 - CreateProfile
    [Documentation]  Create DL Gen9 and Gen10 Server Profile
    ${resp_list}=  Add Server Profiles From Variable  ${create_sp}
    Wait for Task2  ${resp_list}  timeout=600  interval=15

OVF4102 - Password to short Profile OVTC37091
    [Documentation]   Edit an existing server profile to change iLO password
    Run Negative Tasks for List  ${edit_sp_short}  timeout=60    interval=10

OVF4102 - Password to long Profile OVTC37093
    [Documentation]   Edit an existing server profile to change iLO password
    Run Negative Tasks for List  ${edit_sp_long}  timeout=60    interval=10

OVF4102 - CreateTemplate
    [Documentation]  Create DL Gen9  Server Profile Template
    ${resp_list}=  Add Server Profile Templates from variable  ${create_spt}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF4102 - EditTemplate
    [Documentation]  Edit Server Profile Template set password too long and to short
    Run Negative Tasks for List    ${edit_spt_short_long}

OVF4102 - Delete Account OVTC37099
    [Documentation]   Edit an existing server profile template to change iLO password
    ${resp_list}  Edit Server Profiles From Variable    ${edit_sp_delete_admin}
    Wait for Task2  ${resp_list}  timeout=300  interval=10

OVF4102 - Add account back
    [Documentation]   Edit an existing server profile template to change iLO password
    ${resp_list}  Edit Server Profiles From Variable    ${edit_sp_valid_password}
    Wait for Task2  ${resp_list}  timeout=300  interval=10

*** Keywords ***
OVF4102 - Setup
    [Documentation]    Setup
    Set Log Level	TRACE
    Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

OVF4102 - Teardown
    [Documentation]   Clean up Profiles created and turn off power I turned on
    Power off Servers in Profiles  ${create_sp}
    ${sptlist}  remove server profiles from variable  ${create_sp}
    Wait For Task2    ${sptlist}    timeout=600    interval=10
    ${resp_list}=  Remove Server Profile Templates from variable  ${create_spt}
    Run Keyword and Ignore Error  Wait for Task2  ${resp_list}  timeout=240  interval=10

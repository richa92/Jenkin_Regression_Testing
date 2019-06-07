*** Settings ***
Documentation                   OVF706 Gen10 Support multiple URLs for BIOs settings

Library             FusionLibrary
Library             BuiltIn
Library             Collections
Library             json
Library             Dialogs
Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
...                 AND     Remove all Profiles and Templates
Suite Teardown      Run Keywords    Remove all Profiles and Templates
...                 AND     Fusion Api Logout Appliance

*** Variables ***
#${DATA_FILE}         wpst20_variables.py
#${X_API_VERSION}     500

*** Test Cases ***

OVF706 TS1 - Create Profile
    [Tags]  Performance  gen10-condition-BIOS  SP  TS1
    Power Off Servers in Profiles  ${ts1_create_profiles}
    ${resp_list} =  Add Server Profiles from variable  ${ts1_create_profiles}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10

OVF706 TS1 - Power on the Servers and Boot to POST after Create
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_create_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts1_create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF706 TS1 - Verify BIOs Settings after Create
    [Tags]  SP  TS1
    Verify RIS nodes for list  ${ts1_ris_after_create}

OVF706 TS1 - Edit Profile
    [Tags]  Performance  gen10-condition-BIOS  SP  TS1
    Power Off Servers in Profiles  ${ts1_edit_profiles1}
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_profiles1}
    Wait for Task2  ${resp_list}   timeout=3600  interval=10

OVF706 TS1 - Power on the Servers and Boot to POST after First Edit
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_edit_profiles1}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF706 TS1 - Verify BIOs Settings after First Edit
    [Tags]  SP  TS1
    Verify RIS nodes for list  ${ts1_ris_after_edit1}

OVF706 TS1 - Edit Profile a Second Time
    [Tags]  Performance  gen10-condition-BIOS  SP  TS1
    Power Off Servers in Profiles  ${ts1_edit_profiles2}
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_profiles2}
    Wait for Task2  ${resp_list}   timeout=3600  interval=10

OVF706 TS1 - Power on the Servers and Boot to POST after Second Edit
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_edit_profiles2}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF706 TS1 - Verify BIOs Settings after Second Edit
    [Tags]  SP  TS1
    Verify RIS nodes for list  ${ts1_ris_after_edit2}

OVF706 TS1 - Edit Profile a Third Time
    [Tags]  Performance  gen10-condition-BIOS  SP  TS1
    Power Off Servers in Profiles  ${ts1_edit_profiles3}
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_profiles3}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10

OVF706 TS1 - Power on the Servers and Boot to POST after Third Edit
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_edit_profiles3}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles3}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF706 TS1 - Verify BIOs Settings after Third Edit
    [Tags]  SP  TS1
    Verify RIS nodes for list  ${ts1_ris_after_edit3}

OVF706 TS1 - Delete Created Resources
    [Tags]  SP  TS1
    Power Off Servers in Profiles  ${ts1_edit_profiles3}
    ${resp_list}=  Remove Server Profiles from variable	 ${ts1_edit_profiles3}  force=${True}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10

OVF706 TS2 - Create Profile Template
    [Tags]  SPT  TS2
    ${resp_list} =  Add Server Profile Templates from variable  ${ts2_create_profiles_template}
    Wait for Task2  ${resp_list}   timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_create_profiles_template}

OVF706 TS2 - Edit Profile Template
    [Tags]  SPT  TS2
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts2_edit_profiles1_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_edit_profiles1_template}

OVF706 TS2 - Edit Profile Template a Second Time
    [Tags]  SPT  TS2
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts2_edit_profiles2_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_edit_profiles2_template}

OVF706 TS2 - Edit Profile Template a Third Time
    [Tags]  SPT  TS2
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts2_edit_profiles3_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_edit_profiles3_template}

OVF706 TS2 - Delete Created Resources
    [Tags]  SPT  TS2
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts2_edit_profiles3_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF706 TS3 - Create Profile from Template
    [Tags]  Performance  gen10-condition-BIOS  SP-from-SPT  TS3
    ${resp_list} =  Add Server Profile Templates from variable  ${ts2_create_profiles_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_create_profiles_template}
    Power Off Servers in Profiles  ${create_sp_from_spt}
    ${resp_list}=  Add Server Profiles from variable  ${create_sp_from_spt}
    Wait for Task2  ${resp_list}   timeout=3600  interval=10
    :FOR  ${profile}  IN  @{create_sp_from_spt}
    \   Verify Server Profile  ${profile}

OVF706 TS3 - Verify Compliance after Create from Template
    [Tags]  SP-from-SPT  TS3  COMPLIANCE
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

OVF706 TS3 - Edit Profile to be Non-Compliant
    [Tags]  Performance  gen10-condition-BIOS  SP-from-SPT  TS3
    Power Off Servers in Profiles  ${edit_sp_non_compliant}
    ${resp_list}=  Edit Server Profiles from variable  ${edit_sp_non_compliant}
    Wait for Task2  ${resp_list}   timeout=3600  interval=10
    :FOR  ${profile}  IN  @{edit_sp_non_compliant}
    \   Verify Server Profile  ${profile}

OVF706 TS3 - Verify Non-Compliance after Profile Edit
    [Tags]  SP-from-SPT  TS3  COMPLIANCE
    :FOR  ${profile}  IN  @{sp_non_compliant1}
    \   Verify Server Profile Compliance  ${profile}

OVF706 TS3 - Edit Profile to be Compliant
    [Tags]  Performance  gen10-condition-BIOS  SP-from-SPT  TS3
    Power Off Servers in Profiles  ${create_sp_from_spt}
    ${resp_list}=  Edit Server Profiles from variable  ${create_sp_from_spt}
    Wait for Task2  ${resp_list}   timeout=3600  interval=10
    :FOR  ${profile}  IN  @{create_sp_from_spt}
    \   Verify Server Profile  ${profile}

OVF706 TS3 - Verify Compliance after Profile Edit
    [Tags]  SP-from-SPT  TS3  COMPLIANCE
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

OVF706 TS3 - Edit Template to be Non-Compliant
    [Tags]  SP-from-SPT  TS3
    ${resp_list}=  Edit Server Profile Templates from variable  ${edit_spt_non_compliant}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${edit_spt_non_compliant}

OVF706 TS3 - Verify Non-Compliance after Template Edit
    [Tags]  SP-from-SPT  TS3  COMPLIANCE
    :FOR  ${profile}  IN  @{sp_non_compliant2}
    \   Verify Server Profile Compliance  ${profile}

OVF706 TS3 - Edit Template to be Compliant
    [Tags]  SP-from-SPT  TS3
    ${resp_list}=  Edit Server Profile Templates from variable  ${ts2_create_profiles_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_create_profiles_template}

OVF706 TS3 - Verify Compliance after Template Edit
    [Tags]  SP-from-SPT  TS3  COMPLIANCE
    :FOR  ${profile}  IN  @{sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

OVF706 TS3 - Delete Created Resources
    [Tags]  SP-from-SPT  TS3
    Power Off Servers in Profiles  ${create_sp_from_spt}
    ${resp_list}=  Remove Server Profiles from variable	 ${create_sp_from_spt}  force=${True}
    Wait for Task2  ${resp_list}  timeout=3600  interval=10
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts2_create_profiles_template}
    Wait for Task2  ${resp_list}  timeout=60  interval=10

OVF706 TS4 - Negative Template Validation Tests
    [Tags]  SPT  TS4  NEGATIVE
    Run Negative Tasks for List  ${negative_spt_tasks}

OVF706 TS0 - Negative Profile Validation Tests
    [Tags]  SP  TS0  NEGATIVE
    Run Negative Tasks for List  ${negative_tasks}

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Remove all Profiles and Templates
    [Documentation]  Power off all servers, remove all SP's and, remove all SPT's
    Power off ALL servers
    ${resplist} =    Remove All Server Profiles Async    force=${True}
    Wait For Task2    ${resplist}    timeout=3600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=60    interval=5

*** Settings ***
Documentation                   OVF1308 Update PXE boot policy options for Gen10

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

*** Test Cases ***
OVF1308 TS0 - Negative Profile Validation Tests
    [Tags]  SP  TS0  NEGATIVE
    ${resp_list} =  Add Server Profiles from variable  ${ts0_create_profiles}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10
    Run Negative Tasks for List  ${negative_profile_tasks}
    ${resp_list}=  Remove Server Profiles from variable	 ${ts0_create_profiles}  force=${True}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

OVF1308 TS1 - Create Profile
    [Tags]  Performance  gen10-condition-BIOS  SP  TS1
    Power Off Servers in Profiles  ${ts1_create_profiles}
    ${resp_list} =  Add Server Profiles from variable  ${ts1_create_profiles}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts1_create_profiles}
    \   Verify Server Profile  ${profile}

OVF1308 TS1 - Power on the Servers and Boot to POST after Create
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_create_profiles}
    Wait for Servers in Profiles to reach POST State  ${ts1_create_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF1308 TS1 - Verify BIOs Settings after Create
    [Tags]  SP  TS1
    Verify RIS nodes for list  ${ts1_ris_after_create}

OVF1308 TS1 - Edit Profile
    [Tags]  Performance  gen10-condition-BIOS  SP  TS1
    Power Off Servers in Profiles  ${ts1_edit_profiles1}
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_profiles1}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts1_edit_profiles1}
    \   Verify Server Profile  ${profile}

OVF1308 TS1 - Power on the Servers and Boot to POST after First Edit
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_edit_profiles1}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles1}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF1308 TS1 - Verify BIOs Settings after First Edit
    [Tags]  SP  TS1
    Verify RIS nodes for list  ${ts1_ris_after_edit1}

OVF1308 TS1 - Edit Profile a Second Time
    [Tags]  Performance  gen10-condition-BIOS  SP  TS1
    Power Off Servers in Profiles  ${ts1_edit_profiles2}
    ${resp_list} =  Edit Server Profiles from variable  ${ts1_edit_profiles2}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts1_edit_profiles2}
    \   Verify Server Profile  ${profile}

OVF1308 TS1 - Power on the Servers and Boot to POST after Second Edit
    [Tags]  SP  TS1
    Power on Servers in Profiles  ${ts1_edit_profiles2}
    Wait for Servers in Profiles to reach POST State  ${ts1_edit_profiles2}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF1308 TS1 - Verify BIOs Settings after Second Edit
    [Tags]  SP  TS1
    Verify RIS nodes for list  ${ts1_ris_after_edit2}

OVF1308 TS1 - Delete Created Resources
    [Tags]  SP  TS1
    Power Off Servers in Profiles  ${ts1_edit_profiles2}
    ${resp_list}=  Remove Server Profiles from variable	 ${ts1_edit_profiles2}  force=${True}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

OVF1308 TS2 - Create Profile Template
    [Tags]  SPT  TS2
    ${resp_list} =  Add Server Profile Templates from variable  ${ts2_create_profiles_template}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_create_profiles_template}

OVF1308 TS2 - Edit Profile Template
    [Tags]  SPT  TS2
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts2_edit_profiles1_template}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_edit_profiles1_template}

OVF1308 TS2 - Edit Profile Template a Second Time
    [Tags]  SPT  TS2
    ${resp_list} =  Edit Server Profile Templates from variable  ${ts2_edit_profiles2_template}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_edit_profiles2_template}

OVF1308 TS3 - Negative Profile Template Validation Tests
    [Tags]  SPT  TS3  NEGATIVE
    ${resp_list} =  Add Server Profile Templates from variable  ${ts3_create_profile_templates}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Run Negative Tasks for List  ${negative_template_tasks}
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts3_create_profile_templates}
    Wait For Task2  ${resp_list}  timeout=60  interval=10

OVF1308 TS4 - Create Profiles from Template
    [Tags]  Performance  gen10-condition-BIOS  SP-from-SPT  TS4
    Power Off Servers in Profiles  ${ts4_create_sp_from_spt}
    ${resp_list}=  Add Server Profiles from variable  ${ts4_create_sp_from_spt}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts4_create_sp_from_spt}
    \   Verify Server Profile  ${profile}

OVF1308 TS4 - Verify Profile/Template Compliance after Create from Template
    [Tags]  SP-from-SPT  TS4
    :FOR  ${profile}  IN  @{ts4_sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

OVF1308 TS4 - Power on the Profiles and Boot to POST after Create from Template
    [Tags]  SP-from-SPT  TS4
    Power on Servers in Profiles  ${ts4_create_sp_from_spt}
    Wait for Servers in Profiles to reach POST State  ${ts4_create_sp_from_spt}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=15m  interval=10s

OVF1308 TS4 - Verify the Server Settings with RIS after Create from Template
    [Tags]  SP-from-SPT  TS4
    Verify RIS nodes for list  ${ts4_ris_after_create_from_spt}

OVF1308 TS5 - Edit the Profiles to be Non-Compliant
    [Tags]  Performance  gen10-condition-BIOS  SP-from-SPT  TS5  COMPLIANCE
    Power Off Servers in Profiles  ${ts5_edit_sp_non_compliant}
    ${resp_list}=  Edit Server Profiles from variable  ${ts5_edit_sp_non_compliant}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts5_edit_sp_non_compliant}
    \   Verify Server Profile  ${profile}

OVF1308 TS5 - Verify Profile/Template Non-Compliance after Profile Edit
    [Tags]  SP-from-SPT  TS5  COMPLIANCE
    :FOR  ${profile}  IN  @{ts5_sp_non_compliant1}
    \   Verify Server Profile Compliance  ${profile}

OVF1308 TS5 - Edit the Profiles to be Compliant
    [Tags]  Performance  gen10-condition-BIOS  SP-from-SPT  TS5  COMPLIANCE
    Power Off Servers in Profiles  ${ts4_create_sp_from_spt}
    ${resp_list}=  Edit Server Profiles from variable  ${ts4_create_sp_from_spt}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10
    :FOR  ${profile}  IN  @{ts4_create_sp_from_spt}
    \   Verify Server Profile  ${profile}

OVF1308 TS5 - Verify Profile/Template Compliance after Profile Edit
    [Tags]  SP-from-SPT  TS5  COMPLIANCE
    :FOR  ${profile}  IN  @{ts4_sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

OVF1308 TS5 - Edit the Profile Templates to be Non-Compliant
    [Tags]  SP-from-SPT  TS5  COMPLIANCE
    ${resp_list}=  Edit Server Profile Templates from variable  ${ts5_edit_spt_non_compliant}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts5_edit_spt_non_compliant}

OVF1308 TS5 - Verify Profile/Template Non-Compliance after Template Edit
    [Tags]  SP-from-SPT  TS5  COMPLIANCE
    :FOR  ${profile}  IN  @{ts5_sp_non_compliant2}
    \   Verify Server Profile Compliance  ${profile}

OVF1308 TS5 - Edit the Profile Templates to make them Compliant
    [Tags]  SP-from-SPT  TS5  COMPLIANCE
    ${resp_list}=  Edit Server Profile Templates from variable  ${ts2_edit_profiles2_template}
    Wait For Task2  ${resp_list}  timeout=60  interval=10
    Verify Server Profile Templates  ${ts2_edit_profiles2_template}

OVF1308 TS5 - Verify Profile/Template Compliance after Template Edit
    [Tags]  SP-from-SPT  TS5  COMPLIANCE
    :FOR  ${profile}  IN  @{ts4_sp_compliance}
    \   Verify Server Profile Compliance  ${profile}

OVF1308 TS5 - Delete Server Profiles
    [Tags]  SP-from-SPT  TS5  COMPLIANCE
    Power Off Servers in Profiles  ${ts4_create_sp_from_spt}
    ${resp_list}=  Remove Server Profiles from variable	 ${ts4_create_sp_from_spt}  force=${True}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

OVF1308 Delete Templates
    [Tags]  CLEAN-UP
    ${resp_list}=  Remove Server Profile Templates from variable	 ${ts2_edit_profiles2_template}
    Wait For Task2  ${resp_list}  timeout=60  interval=10

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
    Wait For Task2    ${resplist}    timeout=600    interval=5
    ${sptlist} =    Remove All Server Profile Templates
    Wait For Task2    ${sptlist}    timeout=600    interval=5
*** Settings ***
Documentation    Create Verify Delete Profiles for different enclosures using Test template
Resource    resource.txt
Test Template    Profile Tests For All Enclosure

Suite Setup                     QUAL Suite Setup    ${admin_credentials}
Suite Teardown                  QUAL Suite Teardown

*** Test Cases ***

Profile Tests For Enclosure1    profile_template=${server_profile_templates}   expected_profile_template=${expected_server_profile_templates}
    ...    profile=${server_profiles_from_spt}    expected_profile=${expected_server_profiles_from_spt}    sp_fail=${server_profile_many_conn}

Profiles with storage for enclosure1    [Template]    Add Verify Delete Server Profile
    ${server_profile_raid0}    ${expected_server_profile_raid0}    edit_flag=True
    ${server_profile_hba}    ${expected_server_profile_hba}
    ${server_profile_raid1}    ${expected_server_profile_raid1}
    ${server_profile_raid_no_initialize}    ${expected_server_profile_raid_no_initialize}
    ${server_profile_diff_conn}    ${expected_server_profile_diff_conn}
    ${server_profile_three_conn}    ${expected_server_profile_three_conn}

Profile Tests For Enclosure2    profile_template=${server_profile_templates_enc2}   expected_profile_template=${expected_server_profile_templates_enc2}
    ...    profile=${server_profiles_from_spt_enc2}    expected_profile=${expected_server_profiles_from_spt_enc2}    sp_fail=${server_profile_many_conn_enc2}

Profiles with storage for enclosure2    [Template]    Add Verify Delete Server Profile
    ${server_profile_raid0_enc2}    ${expected_server_profile_raid0_enc2}    edit_flag=True
    ${server_profile_hba_enc2}    ${expected_server_profile_hba_enc2}
    ${server_profile_raid1_enc2}    ${expected_server_profile_raid1_enc2}
    ${server_profile_raid_no_initialize_enc2}    ${expected_server_profile_raid_no_initialize_enc2}
    ${server_profile_diff_conn_enc2}    ${expected_server_profile_diff_conn_enc2}
    ${server_profile_three_conn_enc3}    ${expected_server_profile_three_conn_enc2}

Profile Tests For Enclosure3    profile_template=${server_profile_templates_enc3}   expected_profile_template=${expected_server_profile_templates_enc3}
    ...    profile=${server_profiles_from_spt_enc3}    expected_profile=${expected_server_profiles_from_spt_enc3}    sp_fail=${server_profile_many_conn_enc3}

Profiles with storage for enclosure3    [Template]    Add Verify Delete Server Profile
    ${server_profile_raid0_enc3}    ${expected_server_profile_raid0_enc3}    edit_flag=True
    ${server_profile_hba_enc3}    ${expected_server_profile_hba_enc3}
    ${server_profile_raid1_enc3}    ${expected_server_profile_raid1_enc3}
    ${server_profile_raid_no_initialize_enc3}    ${expected_server_profile_raid_no_initialize_enc3}
    ${server_profile_diff_conn_enc3}    ${expected_server_profile_diff_conn_enc3}
    ${server_profile_three_conn_enc3}    ${expected_server_profile_three_conn_enc3}

*** Keywords ***

Profile Tests For All Enclosure
    [Documentation]    Test Cases for Profiles on Enclosure
    [Tags]    PT-ENC
    [Arguments]    ${profile_template}=${server_profile_templates}   ${expected_profile_template}=${expected_server_profile_templates}
    ...    ${profile}=${profiles}    ${expected_profile}=${expected_profiles}    ${sp_fail}=${server_profile_many_conn}
    Log    Profile Tests For Enclosure    console=True
    Base Profile Template Apply Tests    ${profile_template}   ${expected_profile_template}    ${profile}    ${expected_profile}
    Create Server Profiles with Too Many Connections Should Fail    ${sp_fail}
    Log    Server Profiles with Various Local storage configured    console=True
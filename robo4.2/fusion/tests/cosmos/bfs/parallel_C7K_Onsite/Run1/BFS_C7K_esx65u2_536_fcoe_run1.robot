*** Settings ***
Documentation    ESX65U2_536_FCOE
...              Volume origin Existing Volume  OS Version ESX6.7U1
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_536_FCOE  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${esx67u1_536_fcoe_run1_profile_update_spp}
    ${responses}=  Add Server Profiles from variable  ${esx65u2_536_fcoe_run1_profile_data}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${esx65u2_536_fcoe_run1_profile_data_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_536_FCOE  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${esx65u2_536_fcoe_run1_profile_data}

Add Volume To Existing Profile, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_536_FCOE  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${esx65u2_536_fcoe_run1_profile_add_volume}     ${esx65u2_536_fcoe_run1_profile_add_volume_expected}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esx65u2_536_fcoe_run1_profile_add_volume}

Update Firmware And Driver From Server Profiles, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_536_FCOE  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${esx65u2_536_fcoe_run1_profile_update_spp}    ${esx65u2_536_fcoe_run1_profile_update_spp_expected}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esx65u2_536_fcoe_run1_profile_update_spp}

Enable NIC Teaming in ESXi
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_536_FCOE  PRE-IC-EFUSE
    [Documentation]    Enable NIC Teaming in Esxi
    Enable NIC Teaming in ESXi  ${esx65u2_536_fcoe_run1_profile_data}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_536_FCOE  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from ESXi OS should be same   ${esx65u2_536_fcoe_run1_profile_data}

Ping IP Post Action, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  ESX65U2_536_FCOE
   [Documentation]     Ping IP Action, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
   ESXi Server Should Be Pinging And Volume Should Be Active    ${esx65u2_536_fcoe_run1_profile_data}

Remove Server Profile
   [Tags]   R-SP  ESX65U2_536_FCOE
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${esx65u2_536_fcoe_run1_profile_data}
   ${responses}=  Remove Server Profiles from variable  ${esx65u2_536_fcoe_run1_profile_data}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${esx65u2_536_fcoe_run1_profile_data}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Deafult settings
    [Tags]    RESTORE-HW    ESX65U2_536_FCOE
    Power on Servers in Profiles   ${esx65u2_536_fcoe_run1_profile_data}
    Wait for Servers in Profiles to reach POST State  ${esx65u2_536_fcoe_run1_profile_data}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${esx65u2_536_fcoe_run1_profile_data['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    120 seconds
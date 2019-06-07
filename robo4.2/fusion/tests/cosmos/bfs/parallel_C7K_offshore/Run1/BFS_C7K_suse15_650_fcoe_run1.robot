*** Settings ***
Documentation    Interconnect Module FlexFabric-20/40 Adapters 650FLB  Boot type UEFI  Volume origin  New Volume
...              OS Version Suse15
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup And DHCP is Pingable    ${admin_credentials}  ${dhcpservers}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  SLES15_650_FCOE  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${suse15_650_fcoe_run1_profile}
    ${responses}=  Add Server Profiles from variable  ${suse15_650_fcoe_run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${suse15_650_fcoe_run1_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  SLES15_650_FCOE  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${suse15_650_fcoe_run1_profile}

Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  SLES15_650_FCOE  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${suse15_650_fcoe_run1_profile_add_volume}     ${suse15_650_fcoe_run1_profile_add_volume_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${suse15_650_fcoe_run1_profile_add_volume}

Update Firmware From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  SLES15_650_FCOE  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${suse15_650_fcoe_run1_profile_update_spp}    ${suse15_650_fcoe_run1_profile_update_spp_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${suse15_650_fcoe_run1_profile_update_spp}

Enable NIC Teaming in SLES, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  SLES15_650_FCOE  PRE-IC-EFUSE
    [Documentation]    Create NIC Teaming in SLES
    Create SLES Nic Bonding    ${suse15_650_fcoe_run1_profile}
    SLES Server Should Be Pinging And Volume Should Be Active    ${suse15_650_fcoe_run1_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  SLES15_650_FCOE  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from SLES OS should be same   ${suse15_650_fcoe_run1_profile}

Ping IP Post Action, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]      POST  SLES15_650_FCOE
    [Documentation]     Ping IP Post Action, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    SLES Server Should Be Pinging And Volume Should Be Active    ${suse15_650_fcoe_run1_profile_add_volume}

Remove Server Profile
    [Tags]   R-SP  SLES15_650_FCOE
    [Documentation]   Remove Server Profile and verify server profile doesn't exist
    Power off Servers in Profiles  ${suse15_650_fcoe_run1_profile}
    ${responses}=  Remove Server Profiles from variable  ${suse15_650_fcoe_run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Server Profile Should Not Exist  ${suse15_650_fcoe_run1_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW
    Check IloRestTool
    Power on Servers in Profiles   ${suse15_650_fcoe_run1_profile}
    Wait for Servers in Profiles to reach POST State  ${suse15_650_fcoe_run1_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${suse15_650_fcoe_run1_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    60 seconds
    Wait for Servers in Profiles to reach POST State  ${suse15_650_fcoe_run1_profile}  timeout=${timeout}  interval=${interval}

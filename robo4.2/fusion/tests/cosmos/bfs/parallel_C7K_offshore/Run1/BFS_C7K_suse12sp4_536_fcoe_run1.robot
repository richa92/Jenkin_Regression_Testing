*** Settings ***
Documentation    Interconnect Module FlexFabric-20/40 Adapters 536FLB  Boot type UEFI  Volume origin  New Volume
...              OS Version suse12SP4
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup And DHCP is Pingable    ${admin_credentials}  ${dhcpservers}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  SLES12SP4_536_FCOE  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${suse12SP4_536_fcoe_run1_profile}
    ${responses}=  Add Server Profiles from variable  ${suse12SP4_536_fcoe_run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${suse12SP4_536_fcoe_run1_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  SLES12SP4_536_FCOE  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${suse12SP4_536_fcoe_run1_profile}

Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  SLES12SP4_536_FCOE  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${suse12SP4_536_fcoe_run1_profile_add_volume}     ${suse12SP4_536_fcoe_run1_profile_add_volume_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${suse12SP4_536_fcoe_run1_profile_add_volume}

Update Firmware From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  SLES12SP4_536_FCOE  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${suse12SP4_536_fcoe_run1_profile_update_spp}    ${suse12SP4_536_fcoe_run1_profile_update_spp_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${suse12SP4_536_fcoe_run1_profile_update_spp}

Enable NIC Teaming in SLES, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  SLES12SP4_536_FCOE  PRE-IC-EFUSE
    [Documentation]    Create NIC Teaming in SLES, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Create SLES Nic Bonding    ${suse12SP4_536_fcoe_run1_profile}
    SLES Server Should Be Pinging And Volume Should Be Active    ${suse12SP4_536_fcoe_run1_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  SLES12SP4_536_FCOE  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from SLES OS should be same   ${suse12SP4_536_fcoe_run1_profile}

Ping IP Post Action, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  SLES12SP4_536_FCOE
   [Documentation]     Ping IP Post Action, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
   SLES Server Should Be Pinging And Volume Should Be Active    ${suse12SP4_536_fcoe_run1_profile_add_volume}

Remove Server Profile
   [Tags]   R-SP  SLES12SP4_536_FCOE
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${suse12SP4_536_fcoe_run1_profile}
   ${responses}=  Remove Server Profiles from variable  ${suse12SP4_536_fcoe_run1_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${suse12SP4_536_fcoe_run1_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW
    Check IloRestTool
	Power on Servers in Profiles   ${suse12SP4_536_fcoe_run1_profile}
    Wait for Servers in Profiles to reach POST State  ${suse12SP4_536_fcoe_run1_profile}  timeout=${timeout}  interval=${interval} 
    Restore System Defaults Settings    ${rhel76_630_fcoe_run1_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
	Sleep    60 seconds
	Wait for Servers in Profiles to reach POST State  ${suse12SP4_536_fcoe_run1_profile}  timeout=${timeout}  interval=${interval}
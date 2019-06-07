*** Settings ***
Documentation    RHEL76_630_FCOE_Run1
...              Volume origin Existing Volume OS Version RHEL 7.6
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76_630_FCOE  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${rhel76_630_fcoe_run1_profile}
    ${responses}=  Add Server Profiles from variable  ${rhel76_630_fcoe_run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${rhel76_630_fcoe_run1_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${rhel76_630_fcoe_run1_profile}

Add Volume To Existing Profile, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76_630_FCOE  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${rhel76_630_fcoe_run1_profile_add_volume}     ${rhel76_630_fcoe_run1_profile_add_volume_expected}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${rhel76_630_fcoe_run1_profile_add_volume}

Update Firmware And Driver From Server Profiles, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${rhel76_630_fcoe_run1_profile_update_spp}    ${rhel76_630_fcoe_run1_profile_update_spp_expected}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${rhel76_630_fcoe_run1_profile_update_spp}

Enable NIC Teaming in RHEL, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Enable NIC Teaming in RHEL, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    Create RHEL Nic Bonding  ${rhel76_630_fcoe_run1_profile}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${rhel76_630_fcoe_run1_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76_630_FCOE  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from RHEL OS should be same   ${rhel76_630_fcoe_run1_profile}

Ping IP Post Action, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  RHEL76_630_FCOE
   [Documentation]     Ping IP Action, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
   RHEL Server Should Be Pinging And Volume Should Be Active    ${rhel76_630_fcoe_run1_profile}

Remove Server Profile
   [Tags]   R-SP  RHEL76_630_FCOE
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${rhel76_630_fcoe_run1_profile}
   ${responses}=  Remove Server Profiles from variable  ${rhel76_630_fcoe_run1_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${rhel76_630_fcoe_run1_profile}
   
Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW
    Check IloRestTool
	Power on Servers in Profiles   ${rhel76_630_fcoe_run1_profile}
    Wait for Servers in Profiles to reach POST State  ${rhel76_630_fcoe_run1_profile}  timeout=${timeout}  interval=${interval} 
    Restore System Defaults Settings    ${rhel76_630_fcoe_run1_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
	Sleep    60 seconds
	Wait for Servers in Profiles to reach POST State  ${rhel76_630_fcoe_run1_profile}  timeout=${timeout}  interval=${interval}
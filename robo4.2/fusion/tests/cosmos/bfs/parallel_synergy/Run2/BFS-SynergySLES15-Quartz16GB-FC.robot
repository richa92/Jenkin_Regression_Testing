*** Settings ***
Documentation    sles15_quartz16gb_fc_run2_profile_Run2
...              OS Version Suse15
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup And DHCP is Pingable    ${admin_credentials}  ${dhcpservers}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  sles15_quartz16gb_fc  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${sles15_quartz16gb_fc_run2_profile}
    ${responses}=  Add Server Profiles from variable  ${sles15_quartz16gb_fc_run2_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${sles15_quartz16gb_fc_run2_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  sles15_quartz16gb_fc  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${sles15_quartz16gb_fc_run2_profile}

Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  sles15_quartz16gb_fc  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${sles15_quartz16gb_fc_run2_profile_add_volume}     ${sles15_quartz16gb_fc_run2_profile_add_volume_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${sles15_quartz16gb_fc_run2_profile_add_volume}

Update Firmware From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  sles15_quartz16gb_fc  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${sles15_quartz16gb_fc_run2_profile_spp}    ${sles15_quartz16gb_fc_run2_profile_spp_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${sles15_quartz16gb_fc_run2_profile_spp}

Enable NIC Teaming in SLES, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  sles15_quartz16gb_fc  PRE-IC-EFUSE
    [Documentation]    Create NIC Teaming in SLES, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Create SLES Nic Bonding    ${sles15_quartz16gb_fc_run2_profile}
    SLES Server Should Be Pinging And Volume Should Be Active    ${sles15_quartz16gb_fc_run2_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  sles15_quartz16gb_fc  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from SLES OS should be same   ${sles15_quartz16gb_fc_run2_profile}

Ping IP Post Action, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]      POST  sles15_quartz16gb_fc  RSP
    [Documentation]     Ping IP Post Action, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    SLES Server Should Be Pinging And Volume Should Be Active    ${sles15_quartz16gb_fc_run2_profile}

Remove Server Profile
    [Tags]   R-SP  sles15_quartz16gb_fc  RSP
    [Documentation]   Remove Server Profile and verify server profile doesn't exist
    Power off Servers in Profiles  ${sles15_quartz16gb_fc_run2_profile}
    ${responses}=  Remove Server Profiles from variable  ${sles15_quartz16gb_fc_run2_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Server Profile Should Not Exist  ${sles15_quartz16gb_fc_run2_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW  RSP
    Check IloRestTool
    Power on Servers in Profiles   ${sles15_quartz16gb_fc_run2_profile}
    Wait for Servers in Profiles to reach POST State  ${sles15_quartz16gb_fc_run2_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${sles15_quartz16gb_fc_run2_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    60 seconds
    Wait for Servers in Profiles to reach POST State  ${sles15_quartz16gb_fc_run2_profile}  timeout=${timeout}  interval=${interval}

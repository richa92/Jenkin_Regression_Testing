*** Settings ***
Documentation    BFS-Synergy: Sles12SP3_Quiz_FCOE_Run1-testsuite
...              Volume origin Existing Volume  OS Version Sles12SP3
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  Sles12SP3_Quiz_FCOE  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${Sles12SP3_Quiz_FCOE_Run1_profile}
    ${responses}=  Add Server Profiles from variable  ${Sles12SP3_Quiz_FCOE_Run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${Sles12SP3_Quiz_FCOE_Run1_profile}
    Run Keyword If  ${responses} is not ${null}  Get Task Tree From Post Response  ${responses}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  Sles12SP3_Quiz_FCoE  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${Sles12SP3_Quiz_FCOE_Run1_profile}

Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  Sles12SP3_Quiz_FCOE  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${Sles12SP3_Quiz_FCOE_Run1_profile_add_volume}     ${Sles12SP3_Quiz_FCOE_Run1_profile_add_volume_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${Sles12SP3_Quiz_FCOE_Run1_profile_add_volume}

Update Firmware And Driver From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR Sles12SP3_Quiz_FCOE  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${Sles12SP3_Quiz_FCOE_Run1_profile_spp}    ${Sles12SP3_Quiz_FCOE_Run1_profile_spp_expected}  ${fw_timeout}
    SLES Server Should Be Pinging And Volume Should Be Active    ${Sles12SP3_Quiz_FCOE_Run1_profile}

Enable NIC Teaming in SLES, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  Sles12SP3_Quiz_FCOE  PRE-IC-EFUSE
    [Documentation]    Create NIC Teaming in SLES, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    Create SLES Nic Bonding    ${Sles12SP3_Quiz_FCOE_Run1_profile}
    SLES Server Should Be Pinging And Volume Should Be Active    ${Sles12SP3_Quiz_FCOE_Run1_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  Sles12SP3_Quiz_FCOE  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from SLES OS should be same   ${Sles12SP3_Quiz_FCOE_Run1_profile}

Ping IP Post Action Performed, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]    POST  Sles12SP3_Quiz_FCOE
   [Documentation]     Ping IP Post Action Performed, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
   SLES Server Should Be Pinging And Volume Should Be Active    ${Sles12SP3_Quiz_FCOE_Run1_profile}

Remove Server Profile
   [Tags]   R-SP  Sles12SP3_Quiz_FCOE  RSP
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${Sles12SP3_Quiz_FCOE_Run1_profile}
   ${responses}=  Remove Server Profiles from variable  ${Sles12SP3_Quiz_FCOE_Run1_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${Sles12SP3_Quiz_FCOE_Run1_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW    Sles12SP3_Quiz_FCOE  RSP
    Check IloRestTool
    Power on Servers in Profiles   ${Sles12SP3_Quiz_FCOE_Run1_profile}
    Wait for Servers in Profiles to reach POST State  ${Sles12SP3_Quiz_FCOE_Run1_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${Sles12SP3_Quiz_FCOE_Run1_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    60 seconds
    Wait for Servers in Profiles to reach POST State  ${Sles12SP3_Quiz_FCOE_Run1_profile}  timeout=${timeout}  interval=${interval}

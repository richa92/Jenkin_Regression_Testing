*** Settings ***
Documentation    Sles15_QMH2672_FC
...              Volume origin Existing Volume  OS Version Sles15
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  SLES15-QMH2672  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${sles15_QMH2672_fc_run2_profile}
    ${responses}=  Add Server Profiles from variable  ${sles15_QMH2672_fc_run2_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${sles15_QMH2672_fc_run2_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  SLES15-QMH2672  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${sles15_QMH2672_fc_run2_profile}

Add Volume To Existing Profile, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  SLES15-QMH2672  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${sles15_QMH2672_fc_run2_profile_add_volume}     ${sles15_QMH2672_fc_run2_profile_add_volume_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${sles15_QMH2672_fc_run2_profile_add_volume}

Update Firmware And Driver From Server Profiles, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  SLES15-QMH2672  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${sles15_QMH2672_fc_run2_profile_update_spp}    ${sles15_QMH2672_fc_run2_profile_update_spp_expected}
    SLES Server Should Be Pinging And Volume Should Be Active    ${sles15_QMH2672_fc_run2_profile_update_spp}

Enable NIC Teaming in SLES
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  SLES15-QMH2672
    [Documentation]    Create NIC Teaming in SLES
    Create SLES Nic Bonding    ${sles15_QMH2672_fc_run2_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  PRE-IC-EFUSE  SLES15-QMH2672
    [Documentation]     Ethernet MAC Address Verification in OS Level.
    MAC address specified in profile and retrieved from SLES OS should be same   ${sles15_QMH2672_fc_run2_profile}

Ping IP Post Action, SLES Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  SLES15-QMH2672
   [Documentation]     Ping IP Post Action, SLES Server Should Be Pinging And Volume Should Be Active
   SLES Server Should Be Pinging And Volume Should Be Active    ${sles15_QMH2672_fc_run2_profile}

Remove Server Profile
   [Tags]   R-SP  SLES15-QMH2672
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${sles15_QMH2672_fc_run2_profile}
   ${responses}=  Remove Server Profiles from variable  ${sles15_QMH2672_fc_run2_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${sles15_QMH2672_fc_run2_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Deafult settings
    [Tags]    RESTORE-HW    SLES15-QMH2672
    Power on Servers in Profiles   ${sles15_QMH2672_fc_run2_profile}
    Wait for Servers in Profiles to reach POST State  ${sles15_QMH2672_fc_run2_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${sles15_QMH2672_fc_run2_profile['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    120 seconds
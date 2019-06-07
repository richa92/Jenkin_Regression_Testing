*** Settings ***
Documentation    Windows2019_630FLB_FC
...              Volume origin Existing Volume  OS Version Windows2019
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  WIN2019_630FLB_FC  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${win2019_630_fc_run_1_profile}
    ${responses}=  Add Server Profiles from variable  ${win2019_630_fc_run_1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${win2019_630_fc_run_1_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  WIN2019_630FLB_FC  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${win2019_630_fc_run_1_profile}

Add Volume To Existing Profile, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  WIN2019_630FLB_FC  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${win2019_630_fc_run_1_profile_add_volume}     ${win2019_630_fc_run_1_profile_add_volume_expected}
    Windows Server Should Be Pinging And Volume Should Be Active    ${win2019_630_fc_run_1_profile_add_volume}

Update Firmware And Driver From Server Profiles, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  WIN2019_630FLB_FC  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${win2019_630_fc_run_1_profile_update_spp}    ${win2019_630_fc_run_1_profile_update_spp_expected}
    Windows Server Should Be Pinging And Volume Should Be Active    ${win2019_630_fc_run_1_profile_update_spp}

Enable NIC Teaming in Windows
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  WIN2019_630FLB_FC
    [Documentation]    Create NIC Teaming in Windows
    Check And Configure NIC Teaming In Windows    ${win2019_630_fc_run_1_profile}  c     'bond'     Ethernet*

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  PRE-IC-EFUSE  WIN2019_630FLB_FC
    [Documentation]     Ethernet MAC Address Verification in OS Level.
    MAC address specified in profile and retrieved from Windows OS should be same   ${win2019_630_fc_run_1_profile}

Ping IP Post Action, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  WIN2019_630FLB_FC
   [Documentation]     Ping IP Post Action, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   Windows Server Should Be Pinging And Volume Should Be Active    ${win2019_630_fc_run_1_profile}

Remove Server Profile
   [Tags]   R-SP  WIN2019_630FLB_FC
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${win2019_630_fc_run_1_profile}
   ${responses}=  Remove Server Profiles from variable  ${win2019_630_fc_run_1_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${win2019_630_fc_run_1_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Deafult settings
    [Tags]    RESTORE-HW    WIN2019_630FLB_FC
    Power on Servers in Profiles   ${win2019_630_fc_run_1_profile}
    Wait for Servers in Profiles to reach POST State  ${win2019_630_fc_run_1_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${win2019_630_fc_run_1_profile['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    120 seconds
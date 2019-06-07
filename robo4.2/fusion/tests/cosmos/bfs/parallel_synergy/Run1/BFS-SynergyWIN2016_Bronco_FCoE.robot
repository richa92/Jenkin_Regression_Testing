*** Settings ***
Documentation    Windows 2016 bronco fcoe
...              Volume origin Existing Volume  OS Version Win2016, FCOE Connection
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016_B_FcoE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${Win2016_Bronco_FCoE_Run1_profile}
    ${responses}=  Add Server Profiles from variable  ${Win2016_Bronco_FCoE_Run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${Win2016_Bronco_FCoE_Run1_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016_B_FcoE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${Win2016_Bronco_FCoE_Run1_profile}

Add Volume To Existing Profile, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016_B_FcoE
    [Documentation]     Add Volume To Existing Profile, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${Win2016_Bronco_FCoE_Run1_profile_add_volume}     ${Win2016_Bronco_FCoE_Run1_profile_add_volume_expected}
    Windows Server Should Be Pinging And Volume Should Be Active    ${Win2016_Bronco_FCoE_Run1_profile_add_volume}

Update Firmware And Driver From Server Profiles, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016_B_FcoE
    [Documentation]    Update Firmware From Server Profiles, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${Win2016_Bronco_FCoE_Run1_profile_spp}    ${Win2016_Bronco_FCoE_Run1_profile_spp_expected}
    Windows Server Should Be Pinging And Volume Should Be Active    ${Win2016_Bronco_FCoE_Run1_profile_spp}

Enable NIC Teaming in Windows
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016_B_FcoE
    [Documentation]    Create NIC Teaming in Windows
    Check And Configure NIC Teaming In Windows    ${Win2016_Bronco_FCoE_Run1_profile_data}  c     'bond'     Ethernet*
    Install MPIO Feature And Windows Server Should Be Pinging     ${Win2016_Bronco_FCoE_Run1_profile}
    Windows Server Should Be Pinging And Volume Should Be Active  ${Win2016_Bronco_FCoE_Run1_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  PRE-IC-EFUSE  WIN2016_B_FcoE
    [Documentation]     Ethernet MAC Address Verification in OS Level.
    MAC address specified in profile and retrieved from Windows OS should be same   ${Win2016_Bronco_FCoE_Run1_profile}

Ping IP Post Action, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  WIN2016_B_FcoE
   [Documentation]     Ping IP Post Action, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   Windows Server Should Be Pinging And Volume Should Be Active    ${Win2016_Bronco_FCoE_Run1_profile}

Remove Server Profile
   [Tags]   R-SP  WIN2016_B_FcoE
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${Win2016_Bronco_FCoE_Run1_profile}
   ${responses}=  Remove Server Profiles from variable  ${Win2016_Bronco_FCoE_Run1_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${Win2016_Bronco_FCoE_Run1_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW
    Check IloRestTool
    Power on Servers in Profiles   ${Win2016_Bronco_FCoE_Run1_profile}
    Wait for Servers in Profiles to reach POST State  ${Win2016_Bronco_FCoE_Run1_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${Win2016_Bronco_FCoE_Run1_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    60 seconds
    Wait for Servers in Profiles to reach POST State  ${Win2016_Bronco_FCoE_Run1_profile}  timeout=${timeout}  interval=${interval}
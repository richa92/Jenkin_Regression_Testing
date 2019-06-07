*** Settings ***
Documentation    Interconnect HP VC FlexFabric 10Gb/24  Adapters 630 FLB Boot type UEFI
...              Volume origin Existing Volume  OS Version Win2016, FC connection
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016-630FC
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${win2016_fc_630_run1}
    ${responses}=  Add Server Profiles from variable  ${win2016_fc_630_run1}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${win2016_fc_630_run1_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016-630FC
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${win2016_fc_630_run1}

Add Volume To Existing Profile, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016-630FC
    [Documentation]     Add Volume To Existing Profile, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${win2016_fc_630_run1_volume}     ${win2016_fc_630_run1_volume_expected}
    Windows Server Should Be Pinging And Volume Should Be Active    ${win2016_fc_630_run1_volume}

Update Firmware And Driver From Server Profiles, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016-630FC
    [Documentation]    Update Firmware From Server Profiles, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${win2016_fc_630_run1_spp}    ${win2016_fc_630_run1_spp_expected}
    Windows Server Should Be Pinging And Volume Should Be Active    ${win2016_fc_630_run1_spp}

Enable NIC Teaming in Windows
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  WIN2016-630FC
    [Documentation]    Create NIC Teaming in Windows
    Check And Configure NIC Teaming In Windows    ${win2016_fc_630_run1}  c     'bond'     Ethernet*
    
MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  PRE-IC-EFUSE  WIN2016-630FC
    [Documentation]     Ethernet MAC Address Verification in OS Level.
    MAC address specified in profile and retrieved from Windows OS should be same   ${win2016_fc_630_run1}

Ping IP Post Action, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  WIN2016-630FC
   [Documentation]     Ping IP Post Action, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   Windows Server Should Be Pinging And Volume Should Be Active    ${win2016_fc_630_run1_volume}

Remove Server Profile
   [Tags]   R-SP  WIN2016-630FC
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${win2016_fc_630_run1}
   ${responses}=  Remove Server Profiles from variable  ${win2016_fc_630_run1}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${win2016_fc_630_run1}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Deafult settings
    [Tags]    RESTORE-HW    WIN2016-630FC
    Power on Servers in Profiles   ${win2016_fc_630_run1}
    Wait for Servers in Profiles to reach POST State  ${win2016_fc_630_run1}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${win2016_fc_630_run1['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    120 seconds

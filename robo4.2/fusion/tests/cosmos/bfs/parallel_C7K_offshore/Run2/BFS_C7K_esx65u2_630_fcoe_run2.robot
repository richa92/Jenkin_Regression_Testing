*** Settings ***
Documentation    ESX65U2_630_FCOE_Run2
...              Volume origin Existing Volume  OS Version ESX65U2
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_630_FCOE  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${esx65u2_630_fcoe_run2_profile}
    ${responses}=  Add Server Profiles from variable  ${esx65u2_630_fcoe_run2_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${esx65u2_630_fcoe_run2_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${esx65u2_630_fcoe_run2_profile}

Add Volume To Existing Profile, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_630_FCOE  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${esx65u2_630_fcoe_run2_profile_add_volume}     ${esx65u2_630_fcoe_run2_profile_add_volume_expected}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esx65u2_630_fcoe_run2_profile_add_volume}

Update Firmware And Driver From Server Profiles, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${esx65u2_630_fcoe_run2_profile_update_spp}    ${esx65u2_630_fcoe_run2_profile_update_spp_expected}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esx65u2_630_fcoe_run2_profile_update_spp}

Enable NIC Teaming in ESXi, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Enable NIC Teaming in Esxi, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Enable NIC Teaming in ESXi  ${esx65u2_630_fcoe_run2_profile}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esx65u2_630_fcoe_run2_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  ESX65U2_630_FCOE  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from ESXi OS should be same   ${esx65u2_630_fcoe_run2_profile}

Ping IP Post Action, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  ESX65U2_630_FCOE
   [Documentation]     Ping IP Action, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
   ESXi Server Should Be Pinging And Volume Should Be Active    ${esx65u2_630_fcoe_run2_profile}

Remove Server Profile
   [Tags]   R-SP  ESX65U2_630_FCOE
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${esx65u2_630_fcoe_run2_profile}
   ${responses}=  Remove Server Profiles from variable  ${esx65u2_630_fcoe_run2_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${esx65u2_630_fcoe_run2_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW    ESX65U2_630_FCOE
    Check IloRestTool
    Power on Servers in Profiles   ${esx65u2_630_fcoe_run2_profile}
    Wait for Servers in Profiles to reach POST State  ${esx65u2_630_fcoe_run2_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${esx65u2_630_fcoe_run2_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    60 seconds
    Wait for Servers in Profiles to reach POST State  ${esx65u2_630_fcoe_run2_profile}  timeout=${timeout}  interval=${interval}

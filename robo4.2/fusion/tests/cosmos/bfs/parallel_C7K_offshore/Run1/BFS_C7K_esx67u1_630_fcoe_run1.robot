*** Settings ***
Documentation    Esxi67U1_630_FCOE_Run1
...              Volume origin Existing Volume  OS Version ESX6.7U1
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  ESX67U1_630_FCOE  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${esxi67u1_630_fcoe_run1_profile}
    ${responses}=  Add Server Profiles from variable  ${esxi67u1_630_fcoe_run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${esxi67u1_630_fcoe_run1_profile_expected}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  ESX67U1_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${esxi67u1_630_fcoe_run1_profile}

Add Volume To Existing Profile, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  ESX67U1_630_FCOE  PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${esxi67u1_630_fcoe_run1_profile_add_volume}     ${esxi67u1_630_fcoe_run1_profile_add_volume_expected}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esxi67u1_630_fcoe_run1_profile_add_volume}

Update Firmware And Driver From Server Profiles, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  ESX67U1_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${esxi67u1_630_fcoe_run1_profile_update_spp}    ${esxi67u1_630_fcoe_run1_profile_update_spp_expected}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esxi67u1_630_fcoe_run1_profile_update_spp}

Enable NIC Teaming in ESXi, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  ESX67U1_630_FCOE  PRE-IC-EFUSE
    [Documentation]    Enable NIC Teaming in Esxi, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
    Enable NIC Teaming in ESXi  ${esxi67u1_630_fcoe_run1_profile}
    ESXi Server Should Be Pinging And Volume Should Be Active    ${esxi67u1_630_fcoe_run1_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  ESX67U1_630_FCOE  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from ESXi OS should be same   ${esxi67u1_630_fcoe_run1_profile}

Ping IP Post Action, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST  ESX67U1_630_FCOE
   [Documentation]     Ping IP Action, ESXi Server Should Be Pinging, FCoE Disk Should Exist and Active
   ESXi Server Should Be Pinging And Volume Should Be Active    ${esxi67u1_630_fcoe_run1_profile}

Remove Server Profile
   [Tags]   R-SP  ESX67U1_630_FCOE
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${esxi67u1_630_fcoe_run1_profile}
   ${responses}=  Remove Server Profiles from variable  ${esxi67u1_630_fcoe_run1_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${esxi67u1_630_fcoe_run1_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW
    Check IloRestTool
	Power on Servers in Profiles   ${esxi67u1_630_fcoe_run1_profile}
    Wait for Servers in Profiles to reach POST State  ${esxi67u1_630_fcoe_run1_profile}  timeout=${timeout}  interval=${interval} 
    Restore System Defaults Settings    ${esxi67u1_630_fcoe_run1_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
	Sleep    60 seconds
	Wait for Servers in Profiles to reach POST State  ${esxi67u1_630_fcoe_run1_profile}  timeout=${timeout}  interval=${interval}
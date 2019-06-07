*** Settings ***
Documentation    BFS-Synergy: RHEL76-Bronco-ISCSI-testsuite
...              Volume origin Existing Volume  OS Version RHEL 7.6
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76-B-ISCSI  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${rhel76_bronco_iscsi_run1_profile}
    ${responses}=  Add Server Profiles from variable  ${rhel76_bronco_iscsi_run1_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${rhel76_bronco_iscsi_run1_profile_expected}
    Run Keyword If  ${responses} is not ${null}  Get Task Tree From Post Response  ${responses}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76-B-ISCSI  PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${rhel76_bronco_iscsi_run1_profile}

Update Firmware And Driver From Server Profiles, RHEL Server Should Be Pinging, fc Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76-B-ISCSI  PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, RHEL Server Should Be Pinging, fc Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${rhel76_bronco_iscsi_run1_profile_spp}    ${rhel76_bronco_iscsi_run1_profile_spp_expected}  ${fw_timeout}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${rhel76_bronco_iscsi_run1_profile}

Enable NIC Teaming in RHEL
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76-B-ISCSI  PRE-IC-EFUSE
    [Documentation]    Create NIC Teaming in RHEL
    Create RHEL Nic Bonding  ${rhel76_bronco_iscsi_run1_profile}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${rhel76_bronco_iscsi_run1_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  RHEL76-B-ISCSI  PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from RHEL OS should be same   ${rhel76_bronco_iscsi_run1_profile}

Ping IP Post Action Performed, RHEL Server Should Be Pinging, fc Disk Should Exist and Active
   [Tags]    POST  RHEL76-B-ISCSI
   [Documentation]     Ping IP Post Action Performed, RHEL Server Should Be Pinging, fc Disk Should Exist and Active
   RHEL Server Should Be Pinging And Volume Should Be Active    ${rhel76_bronco_iscsi_run1_profile}

Remove Server Profile
   [Tags]   R-SP  RHEL76-B-ISCSI  RSP
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${rhel76_bronco_iscsi_run1_profile_data}
   ${responses}=  Remove Server Profiles from variable  ${rhel76_bronco_iscsi_run1_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${rhel76_bronco_iscsi_run1_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW    RHEL76-B-ISCSI  RSP
    Check IloRestTool
    Power on Servers in Profiles   ${rhel76_bronco_iscsi_run1_profile}
    Wait for Servers in Profiles to reach POST State  ${rhel76_bronco_iscsi_run1_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${rhel76_bronco_iscsi_run1_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    60 seconds
    Wait for Servers in Profiles to reach POST State  ${rhel76_bronco_iscsi_run1_profile}  timeout=${timeout}  interval=${interval}

*** Settings ***
Documentation    BFS-Synergy: RHEL610_Electorn16GB_FC
...              Volume origin Existing Volume  OS Version RHEL 610
Resource                        ../../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test Cases ***
Create Server Profiles with Storage Volumes
    [Tags]    SP  PM  PRE-FO  PRE-FR  PRE-BR  RHEL610-E-FC  PRE-IC-EFUSE
    [Documentation]  Create Server Profiles for BL servers with SAN Storage
    Power off Servers in Profiles  ${RHEL610_Electorn16GB_FC_Run2_profile}
    ${responses}=  Add Server Profiles from variable  ${RHEL610_Electorn16GB_FC_Run2_profile}
    Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
    Verify Resources for List  ${RHEL610_Electorn16GB_FC_Run2_profile_expected}
    Run Keyword If  ${responses} is not ${null}  Get Task Tree From Post Response  ${responses}

Power On server Profile And Wait For Post State
    [Tags]    SP-ON  PM  PRE-FO  PRE-FR  PRE-BR  RHEL610-E-FC   PRE-IC-EFUSE
    [Documentation]    Power On Server Profile And Wait For Post State
    Power On Server Profile And Wait For POST State    ${RHEL610_Electorn16GB_FC_Run2_profile}

Add Volume To Existing Profile, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    ADD-VOL  PM  PRE-FO  PRE-FR  PRE-BR  RHEL610-E-FC   PRE-IC-EFUSE
    [Documentation]     Add Volume To Existing Profile, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile And Power On    ${RHEL610_Electorn16GB_FC_Run2_profile_add_volume}     ${RHEL610_Electorn16GB_FC_Run2_profile_add_volume_expected}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${RHEL610_Electorn16GB_FC_Run2_profile_add_volume}

Update Firmware And Driver From Server Profiles, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    [Tags]    UPDATE-SP  PM  PRE-FO  PRE-FR  PRE-BR  RHEL610-E-FC   PRE-IC-EFUSE
    [Documentation]    Update Firmware From Server Profiles, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
    Edit Server Profile, Wait until firmware state reaches to desired state     ${RHEL610_Electorn16GB_FC_Run2_profile_spp}    ${RHEL610_Electorn16GB_FC_Run2_profile_spp_expected}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${RHEL610_Electorn16GB_FC_Run2_profile_spp}

Enable NIC Teaming in RHEL
    [Tags]    NIC  PM  PRE-FO  PRE-FR  PRE-BR  RHEL610-E-FC   PRE-IC-EFUSE
    [Documentation]    Create NIC Teaming in RHEL
    Create RHEL Nic Bonding  ${RHEL610_Electorn16GB_FC_Run2_profile}
    RHEL Server Should Be Pinging And Volume Should Be Active    ${RHEL610_Electorn16GB_FC_Run2_profile}

MAC address specified in profile and retrieved from OS should be same
    [Tags]    V-MAC  PM  PRE-FO  PRE-FR  PRE-BR  RHEL610-E-FC   PRE-IC-EFUSE
    [Documentation]     Ethernet MAC Address Verification in OS Level
    MAC address specified in profile and retrieved from RHEL OS should be same   ${RHEL610_Electorn16GB_FC_Run2_profile}

Ping IP Post Action Performed, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]    POST  RHEL610-E-FC
   [Documentation]     Ping IP Post Action Performed, RHEL Server Should Be Pinging, FCoE Disk Should Exist and Active
   RHEL Server Should Be Pinging And Volume Should Be Active    ${RHEL610_Electorn16GB_FC_Run2_profile}

Remove Server Profile
   [Tags]   R-SP  RHEL610-E-FC  RSP
   [Documentation]   Remove Server Profile and verify server profile doesn't exist
   Power off Servers in Profiles  ${RHEL610_Electorn16GB_FC_Run2_profile}
   ${responses}=  Remove Server Profiles from variable  ${RHEL610_Electorn16GB_FC_Run2_profile}
   Run Keyword If  ${responses} is not ${null}  Wait For Task2  ${responses}
    ...  timeout=2000  interval=5
   Server Profile Should Not Exist  ${RHEL610_Electorn16GB_FC_Run2_profile}

Restore System Default Settings for Servers
    [Documentation]    Restore Servers to System Default settings
    [Tags]    RESTORE-HW  RSP
    Check IloRestTool
    Power on Servers in Profiles   ${RHEL610_Electorn16GB_FC_Run2_profile}
    Wait for Servers in Profiles to reach POST State  ${RHEL610_Electorn16GB_FC_Run2_profile}  timeout=${timeout}  interval=${interval}
    Restore System Defaults Settings    ${RHEL610_Electorn16GB_FC_Run2_profile[0]['serverHardwareUri']}    ${ilo_credentials['username']}    ${ilo_credentials['password']}
    Sleep    60 seconds
    Wait for Servers in Profiles to reach POST State  ${RHEL610_Electorn16GB_FC_Run2_profile}  timeout=${timeout}  interval=${interval}

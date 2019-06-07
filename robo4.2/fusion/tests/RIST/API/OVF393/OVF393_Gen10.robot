*** Settings ***
Documentation                   OVF393 FC/FCoE boot 2 targets: Synergy Gen10 FlexFabric CNA

Library             FusionLibrary
Library             BuiltIn
Library             Collections

Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./common_keywords.robot

Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
Suite Teardown      Run Keywords    Initialize Appliance For Test Case
...                 AND    Fusion Api Logout Appliance

*** Variables ***

*** Test Cases ***

OVF393 TC1 - Create and Verify UEFI 2 target FCoE Boot Profile
    [Tags]  SP  TC1
   Initialize Appliance For Test Case

    ${resp_list} =  Add Server Profiles from variable  ${Gen10_ts1_create_UEFI_profiles}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

#   From Bill Skinner 8/6/18
#   Hi Ron,
#
#   I set up trippel.ftc.rdlabs.hpecorp.net, ran the OVF393 tests.
#   Test was failing, wasn't seeing the second target. Talked to Dave Arko, the second target's been disabled for
#   Bronco/Quiz due to issues with failover to the second target when connecting with Nimble.  This functionality is
#   supposed to be fixed in Havana release, at which time 2 targets will be re-enabled.  2 targets will be available
#   when Quack is released as far as we know now.  I think it would be useful to modify the OVF393 RG tests to verify
#   that a second target is not being added to the created SP until we get second target in Havana.
#
#   Bill (this email was From Bill Skinner)
#
#   (RS) Thus the tests will check 'targets' lists length and it should equal 1 until Havana.
#   For Havana uncomment: "until Havana" lines and comment (or remove: Verify Against Storage System Pre Havana

    # Collect values from the created Server Profile
    ${sp}=  Get Resource  SP:${PROFILE1_UEFI_NAME}
    ${pconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Primary
    ${p_target_length} =    Get Length    ${pconn['boot']['targets']}
    Should Be Equal As Integers    1    ${p_target_length}

    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
# until Havana    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}

    ${sconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Secondary
    ${s_target_length} =    Get Length    ${sconn['boot']['targets']}
    Should Be Equal As Integers    1    ${s_target_length}

    ${starget1}=  Set Variable  ${sconn['boot']['targets'][0]}
# until Havana    ${starget2}=  Set Variable  ${sconn['boot']['targets'][1]}

    Verify Against Storage System PreHavana  ${sp}  ${ptarget1}  ${starget1}
# until Havana    Verify Against Storage System  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    ${ris}=  Get RIS Node  ${ris_node_Gen10}

    WWNs Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][0]['Wwn']}
    Should Be Equal  ${ptarget1['lun']}        ${ris['DesiredBootDevices'][0]['Lun']}

    WWNs Should Be Equal  ${starget1['arrayWwpn']}  ${ris['DesiredBootDevices'][1]['Wwn']}
    Should Be Equal  ${starget1['lun']}        ${ris['DesiredBootDevices'][1]['Lun']}

# until Havana
#    WWNs Should Be Equal  ${ptarget2['arrayWwpn']}  ${ris['DesiredBootDevices'][2]['Wwn']}
#    Should Be Equal  ${ptarget2['lun']}        ${ris['DesiredBootDevices'][2]['Lun']}

#    WWNs Should Be Equal  ${starget2['arrayWwpn']}  ${ris['DesiredBootDevices'][3]['Wwn']}
#    Should Be Equal  ${starget2['lun']}        ${ris['DesiredBootDevices'][3]['Lun']}

OVF393 TC2 - Create and Verify BIOS 2 target FCoE Boot Profile
    [Tags]  SP  TC2  OVD19687
    Initialize Appliance For Test Case

    ${resp_list} =  Add Server Profiles from variable  ${Gen10_ts1_create_BIOS_profiles}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    # Need to go through this set of POST states to get to final server state with valid boot info
    Power on Servers in Profiles  ${Gen10_ts1_create_BIOS_profiles}
    Wait for Servers in Profiles to reach POST State  ${Gen10_ts1_create_BIOS_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=30m  interval=10s
    Wait for Servers in Profiles to reach POST State  ${Gen10_ts1_create_BIOS_profiles}  post_state=IN_POST  timeout=30m  interval=10s
    Wait for Servers in Profiles to reach POST State  ${Gen10_ts1_create_BIOS_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=30m  interval=10s

    # Collect values from the created Server Profile
    ${sp}=  Get Resource  SP:${PROFILE1_BIOS_NAME}
    ${pconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Primary
    ${p_target_length} =    Get Length    ${pconn['boot']['targets']}
    Should Be Equal As Integers    1    ${p_target_length}
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
# until Havana    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}

    ${sconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Secondary
    ${p_target_length} =    Get Length    ${pconn['boot']['targets']}
    Should Be Equal As Integers    1    ${p_target_length}
    ${starget1}=  Set Variable  ${sconn['boot']['targets'][0]}
# until Havana    ${starget2}=  Set Variable  ${sconn['boot']['targets'][1]}

    Verify Against Storage System PreHavana  ${sp}  ${ptarget1}  ${starget1}
# until Havana    Verify Against Storage System  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    ${server_ip}=  Get Server Hardware iLO IP  ${ENC2SHBAY6}
    ${cqhord}=  Run cpqlocfg and Get CQHORD  ${server_ip}
    ${bco}=  get ilo legacy bios boot controller order  ${cqhord}
    ${bco_0}=  Get From List  ${bco}  0
    ${vid}=  Get From Dictionary  ${bco_0}  vendor_id
    ${did}=  Get From Dictionary  ${bco_0}  device_id
    ${slot}=  Get From Dictionary  ${bco_0}  slot
    Should Be Equal  ${vid}  ${HP_PCI_VENDOR_ID}  Non-HP device found for first boot option
    List Should Contain Value  ${VALID_FCOE_PCI_DEVICE_IDS}  ${did}  Non-FCOE device found for first boot option
    Should Be Equal  ${slot}  ${FCOE_DEVICE_MEZZ_SLOT}  Incorrect slot for first boot option

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Initialize Appliance For Test Case
    [Documentation]  Initialize the appliance state
    Power Off Server  ${ENC2SHBAY6}  powerControl=PressAndHold
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_uris_Gen10}
    Wait For Task2  ${task}  timeout=600  interval=10

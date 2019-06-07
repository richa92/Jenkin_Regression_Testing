*** Settings ***
Documentation                   OVF387 FC boot 2 targets: Synergy Gen10 FC HBA - UEFI & BIOS modes

Library             FusionLibrary
Library             BuiltIn
Library             Collections

Resource            ../global_variables.robot
Resource            ./../../../../Resources/api/fusion_api_resource.txt
Resource            ./common_keywords.robot

Variables           ${DATA_FILE}

Suite Setup         Run Keywords    Initialize the Variables and Log In as Administrator
...                 AND     Set Suite Variable    ${WFT2_CONTINUE_ON_ERROR}    ${TRUE}
Suite Teardown      Run Keywords     Initialize Appliance For Test Case
...                 AND    Fusion Api Logout Appliance


*** Variables ***

*** Test Cases ***

OVF387 TC1 - Create and Verify UEFI 2 target FC Boot Profile
    [Tags]  SP  TC1
   Initialize Appliance For Test Case

    ${resp_list} =  Add Server Profiles from variable  ${OVF387_create_UEFI_profiles}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    # Collect values from the created Server Profile
    ${sp}=  Get Resource  SP:${PROFILE1_UEFI_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    ${pconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Primary
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}
    ${sconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Secondary
    ${starget1}=  Set Variable  ${sconn['boot']['targets'][0]}
    ${starget2}=  Set Variable  ${sconn['boot']['targets'][1]}

    Verify Against Storage System  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    ${ris}=  Get RIS Node  ${ris_nodeGen10}

    WWNs Should Be Equal  ${ptarget1['arrayWwpn']}  ${ris['DesiredBootDevices'][0]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][0]['Lun']}
    Should Be Equal  ${ptarget1['lun']}        ${nrislun}

    WWNs Should Be Equal  ${starget1['arrayWwpn']}  ${ris['DesiredBootDevices'][1]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][1]['Lun']}
    Should Be Equal  ${starget1['lun']}        ${nrislun}

    WWNs Should Be Equal  ${ptarget2['arrayWwpn']}  ${ris['DesiredBootDevices'][2]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][2]['Lun']}
    Should Be Equal  ${ptarget2['lun']}        ${nrislun}

    WWNs Should Be Equal  ${starget2['arrayWwpn']}  ${ris['DesiredBootDevices'][3]['Wwn']}
    ${nrislun}=  Normalize RIS FC LUN  ${ris['DesiredBootDevices'][3]['Lun']}
    Should Be Equal  ${starget2['lun']}        ${nrislun}

OVF387 TC2 - Create and Verify BIOS 2 target FC Boot Profile
    [Tags]  SP  TC2  OVD19687
    Initialize Appliance For Test Case

    ${resp_list} =  Add Server Profiles from variable  ${OVF387_create_BIOS_profiles}
    Wait For Task2  ${resp_list}  timeout=3600  interval=10

    # Need to go through this set of POST states to get to final server state with valid boot info
    Power on Servers in Profiles  ${OVF387_create_BIOS_profiles}
    Wait for Servers in Profiles to reach POST State  ${OVF387_create_BIOS_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=30m  interval=10s
    Wait for Servers in Profiles to reach POST State  ${OVF387_create_BIOS_profiles}  post_state=IN_POST  timeout=30m  interval=10s
    Wait for Servers in Profiles to reach POST State  ${OVF387_create_BIOS_profiles}  post_state=IN_POST_DISCOVERY_COMPLETE|FINISHED_POST  timeout=30m  interval=10s

    # Collect values from the created Server Profile
    ${sp}=  Get Resource  SP:${PROFILE1_BIOS_NAME}
    ${connections}=  Set Variable  ${sp["connectionSettings"]["connections"]}
    ${pconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Primary
    ${ptarget1}=  Set Variable  ${pconn['boot']['targets'][0]}
    ${ptarget2}=  Set Variable  ${pconn['boot']['targets'][1]}
    ${sconn}=  Get Connection by Boot Priority  ${sp["connectionSettings"]["connections"]}  Secondary
    ${starget1}=  Set Variable  ${sconn['boot']['targets'][0]}
    ${starget2}=  Set Variable  ${sconn['boot']['targets'][1]}

    Verify Against Storage System  ${sp}  ${ptarget1}  ${ptarget2}  ${starget1}  ${starget2}

    # Verify that the server is configured correctly
    ${server_ip}=  Get Server Hardware iLO IP  ${ENC2SHBAY6}
    ${cqhord}=  Run cpqlocfg and Get CQHORD  ${server_ip}
    ${bco}=  get ilo legacy bios boot controller order  ${cqhord}
    ${bco_0}=  Get From List  ${bco}  0
    ${vid}=  Get From Dictionary  ${bco_0}  vendor_id
    ${did}=  Get From Dictionary  ${bco_0}  device_id
    ${slot}=  Get From Dictionary  ${bco_0}  slot
    Should Be Equal  ${vid}  ${HP_PCI_VENDOR_ID}  Non-HP device found for first boot option
    List Should Contain Value  ${VALID_FC_PCI_DEVICE_IDS}  ${did}  Non-FC device found for first boot option
    Should Be Equal  ${slot}  ${FC_DEVICE_MEZZ_SLOT}  Incorrect slot for first boot option

*** Keywords ***
Initialize the Variables and Log In as Administrator
    [Documentation]  Set the log level to TRACE, initialize the variables and, login as Administrator
    Set Log Level   TRACE
    log variables
    Fusion Api Login Appliance  ${APPLIANCE_IP}  ${admin_credentials}

Initialize Appliance For Test Case
    [Documentation]  Initialize the appliance state
    Power Off Server  ${ENC2SHBAY6}  powerControl=PressAndHold
    ${task}=  Remove Server Profiles by Server Hardware  ${server_hardware_urisGen10}
    Wait For Task2  ${task}  timeout=600  interval=10

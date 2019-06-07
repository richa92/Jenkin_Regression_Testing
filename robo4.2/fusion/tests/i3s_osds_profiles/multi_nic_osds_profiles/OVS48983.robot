*** Settings ***
Documentation     Multi nic osds profiles - SPT

Resource          ../../../Resources/api/fusion_api_resource.txt
Resource          resource.robot
Suite Setup       Login to Fusion Via REST    ${fusion_ip}    ${admin_credentials}
Suite Teardown    Fusion Api Logout Appliance

*** Test Cases ***
OVTC57513
    [Documentation]    Create SPT with multi-NIC management OSDP using single networks
    [Tags]    TC01    SPT    SINGLE-NW

    ${spt} =    copy.deepcopy    ${OVTC57513_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Should Be True    ${blnCreateSPT}   Failed to create SPT '${spt['name']}'
    [Teardown]    Remove SPT By Name    ${OVTC57513_spt['name']}

OVTC57514
    [Documentation]    Modify multiNIC single network SPT (no SP)
    ...    and change the deployment setting network to a different network
    [Tags]    TC02    SPT    SINGLE-NW
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57514_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57514_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${osds} =    copy.deepcopy    ${spt_osds_with_diff_nws}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57514_spt['name']}

OVTC57515
    [Documentation]    Modify multiNIC single network SPT (no SP) and rename the connections
    [Tags]    TC03    SPT    SINGLE-NW
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57515_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57515_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${conns_with_diff_mgmt_nw_names}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57515_spt['name']}

OVTC57516
    [Documentation]    Modify multiNIC single network SPT (no SP) and Add new connection
    [Tags]    TC04    SPT    SINGLE-NW
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57516_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57516_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${conns_with_extra_mgmt_nw}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57516_spt['name']}

OVTC57517
    [Documentation]    Modify multiNIC single network SPT (no SP) and delete an existing connection
    [Tags]    TC05    SPT    SINGLE-NW
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57517_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57517_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${new_conns} =    Delete Connection By Name    ${spt_dto['connectionSettings']['connections']}    ${new_mgmt_conn[0]['name']}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${new_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57517_spt['name']}

OVTC57519
    [Documentation]    Create SP with multi-NIC management OSDP using single network
    [Tags]    TC07    SP    SINGLE-NW

    ${sp} =    copy.deepcopy    ${OVTC57519_sp}
    # Delete profile if already assigned to HW
    ${server_prof} =    Get Server Hardware Profile    ${sp['serverHardwareUri']}
    Run Keyword If    '${server_prof}'!='${null}'    Run Keywords
    ...    Power Off Profile Server    ${sp['serverHardwareUri']}    AND
    ...    Delete Server Profile    ${server_prof}

    ${blnCreateSP} =    Create I3S Server Profile    ${sp}
    Should Be True    ${blnCreateSP}    Failed to create profile '${sp['name']}'
    [Teardown]    Remove SP By Name    ${OVTC57519_sp['name']}

OVTC57520
    [Documentation]    Modify multiNIC single network SP and choose different single network connection in the OS deployment Setting
    [Tags]    TC08    SP    SINGLE-NW
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57520_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57520_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${osds} =    copy.deepcopy    ${sp_osds_with_diff_nws}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${sp_dto}    osDeploymentSettings=${osds_conns}
    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57520_sp['name']}

OVTC57521
    [Documentation]    Modify multiNIC single network SP and rename the connections
    [Tags]    TC09    SP    SINGLE-NW
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57521_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57521_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${conns_with_diff_mgmt_nw_names}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${sp_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${sp_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57521_sp['name']}

OVTC57522
    [Documentation]    Modify multiNIC single network SP and Add new connection
    [Tags]    TC10    SP    SINGLE-NW
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57522_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57522_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${connections} =    Lookup connection uris    ${conns_with_extra_mgmt_nw}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57522_sp['name']}

OVTC57523
    [Documentation]    Modify multiNIC single network SP and delete an existing connection
    [Tags]    TC11    SP    SINGLE-NW
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57523_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57523_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${new_conns} =    Delete Connection By Name    ${sp_dto['connectionSettings']['connections']}    ${new_mgmt_conn[0]['name']}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${new_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57523_sp['name']}

OVTC57525
    [Documentation]    Create SP from SPT using multi-NIC management OSDP with single network
    [Tags]    TC13    SP-SPT    SINGLE-NW

    ${ovtc57525_spt} =    copy.deepcopy    ${OVTC57513_spt}
    ${ovtc57525_sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${ovtc57525_spt}
    Should Be True    ${blnCreateSPT}    Failed to create SPT '${ovtc57525_spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${ovtc57525_sp}
    Should Be True    ${blnCreateSPFromSPT}    Failed to create profile '${ovtc57525_sp['name']}'
    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${ovtc57525_sp['name']}    AND
    ...    Remove SPT By Name    ${ovtc57525_spt['name']}

OVTC57526
    [Documentation]    Modify multiNIC single network SPT (which has SP created)
    ...    and choose different network in the OS deployment Setting.
    [Tags]    TC14    SPT    SINGLE-NW
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57514_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57514_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${osds} =    copy.deepcopy    ${spt_osds_with_diff_nws}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57514_spt['name']}

OVTC57527
    [Documentation]    Modify multiNIC single network SPT (which has SP created) and rename the connections
    [Tags]    TC15    SPT    SINGLE-NW
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57515_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57515_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${conns_with_diff_mgmt_nw_names}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57515_spt['name']}

OVTC57528
    [Documentation]    Modify multiNIC single network SPT (which has SP created) and Add new connection
    [Tags]    TC16    SPT    SINGLE-NW
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57516_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57516_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${conns_with_extra_mgmt_nw}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'NonCompliant'
    ...    Fail    Profile is Compliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${sp_from_spt['name']}
    Run Keyword If    '${blnUpdateSp}'!='True'    Fail    Failed to Update SP From SPT

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57516_spt['name']}

OVTC57529
    [Documentation]    Modify multiNIC single network SPT (which has SP created) and delete an existing connection
    [Tags]    TC17    SPT    SINGLE-NW
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57517_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57517_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${new_conns} =    Delete Connection By Name    ${spt_dto['connectionSettings']['connections']}    ${new_mgmt_conn[0]['name']}
    ${new_conns} =    Delete Connection By Name    ${spt_dto['connectionSettings']['connections']}    Storage Network
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${new_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57517_spt['name']}

OVTC57530
    [Documentation]    Create SP and SPT using MultiNIC netset and configure different networks (single networks)
    [Tags]    TC18    SP    SPT    SINGLE-NW    NEGATIVE

    ${spt} =    copy.deepcopy    ${OVTC57530_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}

    ${sp} =    copy.deepcopy    ${OVTC57530_sp}
    ${blnCreateSPFromSPT} =    Create I3S Server Profile    ${sp}

    Run Keyword Unless    ${blnCreateSPT}==False and ${blnCreateSPFromSPT}==False    Run Keywords
    ...    Should Not Be True    ${blnCreateSPT}    SPT '${spt['name']}' created successfully    AND
    ...    Should Not Be True    ${blnCreateSPFromSPT}    SP '${sp['name']}' created successfully

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp['name']}    AND
    ...    Remove SPT By Name    ${spt['name']}

OVTC57531
    [Documentation]    Create SPT with multi-NIC management OSDP using network from netset
    [Tags]    TC19    SPT    NET-SET

    ${spt} =    copy.deepcopy    ${OVTC57531_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Should Be True    ${blnCreateSPT}    Failed to create SPT: '${spt['name']}'

    [Teardown]    Remove SPT By Name    ${spt['name']}

OVTC57532
    [Documentation]    Modify multiNIC netset SPT (no SP) and change the
    ...    deployment setting network to a different network from the same netset
    [Tags]    TC20    SPT    NET-SET
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57532_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57532_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${osds} =    copy.deepcopy    ${spt_osds_with_diff_nws_of_netset}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57532_spt['name']}

OVTC57533
    [Documentation]    Modify multiNIC netset SPT (no SP) and choose different netset
    [Tags]    TC21    SPT    NET-SET
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57533_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57533_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${osds} =    copy.deepcopy    ${spt_osds_of_more_netset}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57514_spt['name']}

OVTC57534
    [Documentation]    Modify multiNIC netset SPT (no SP) and rename the connections that are using netset
    [Tags]    TC22    SPT    NET-SET
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57534_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57534_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${netset_conns_with_diff_mgmt_nw_names}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57534_spt['name']}

OVTC57535
    [Documentation]    Modify multiNIC netset SPT (no SP) and replace netset with single network connections
    [Tags]    TC23    SPT    NET-SET    SINGLE-NW
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57535_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57535_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${spt_conn_settings['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${spt_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57535_spt['name']}

OVTC57536
    [Documentation]    Modify multiNIC netset SPT (no SP) and replace single network connections with Netset
    [Tags]    TC24    SPT    NET-SET    SINGLE-NW
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57536_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57536_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${spt_conn_settings_with_netset['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${spt_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57536_spt['name']}

OVTC57537
    [Documentation]    Modify multiNIC netset SPT (no SP) and Add new connection
    [Tags]    TC25    SPT    NET-SET
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57537_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57537_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${netset_conns_with_extra_mgmt_nw}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57537_spt['name']}

OVTC57538
    [Documentation]    Modify multiNIC netset SPT (no SP) and delete an existing connection
    [Tags]    TC27    SPT    NET-SET
    [Setup]    Create SPT with multi-NIC management OSDP    ${OVTC57538_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57538_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers
    ${new_conns} =    Delete Connection By Name    ${spt_dto['connectionSettings']['connections']}    ${new_mgmt_conn[0]['name']}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${new_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5
    [Teardown]    Remove SPT By Name    ${OVTC57538_spt['name']}

OVTC57540
    [Documentation]    Create SP with multi-NIC management OSDP using netset
    [Tags]    TC28    SP    NET-SET

    ${sp} =    copy.deepcopy    ${OVTC57540_sp}
    # Delete profile if already assigned to HW
    ${server_prof} =    Get Server Hardware Profile    ${sp['serverHardwareUri']}
    Run Keyword If    '${server_prof}'!='${null}'    Run Keywords
    ...    Power Off Profile Server    ${sp['serverHardwareUri']}    AND
    ...    Delete Server Profile    ${server_prof}

    ${blnCreateSP} =    Create I3S Server Profile    ${sp}
    Should Be True    ${blnCreateSP}    Failed to create profile '${sp['name']}'
    [Teardown]    Remove SP By Name    ${OVTC57540_sp['name']}

OVTC57541
    [Documentation]    Modify multiNIC netset SP and choose
    ...    different network from the netset in the OS deployment Setting and save
    [Tags]    TC29    SP    NET-SET
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57541_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57541_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${osds} =    copy.deepcopy    ${sp_osds_with_diff_nws_of_netset}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${sp_dto}    osDeploymentSettings=${osds_conns}
    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5

    [Teardown]    Remove SP By Name    ${OVTC57541_sp['name']}

OVTC57542
    [Documentation]    Edit multiNIC netset SP and modify the netset connections to use different netset. 
    [Tags]    TC30    SP    NET-SET
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57542_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57542_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${osds} =    copy.deepcopy    ${sp_osds_of_more_netset}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${sp_dto}    osDeploymentSettings=${osds_conns}
    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57542_sp['name']}

OVTC57543
    [Documentation]    Modify multiNIC netset SP and rename the connections using netset
    [Tags]    TC31    SP    NET-SET
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57543_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57543_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${netset_conns_with_diff_mgmt_nw_names}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57543_sp['name']}

OVTC57544
    [Documentation]    Modify multiNIC netset SP and replace netset with single networks
    [Tags]    TC32    SP    NET-SET
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57544_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57544_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers

    ${conns} =    copy.deepcopy    ${sp_conn_settings['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${sp_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${sp_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57544_sp['name']}

OVTC57545
    [Documentation]    Modify multiNIC netset SPT and replace single network connection with Netset
    [Tags]    TC33    SPT    NET-SET
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57545_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57545_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${sp_conn_settings_with_netset['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${sp_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${sp_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57545_sp['name']}

OVTC57546
    [Documentation]    Modify multiNIC netset SP and Add new connection
    [Tags]    TC34    SP    NET-SET
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57546_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57546_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${conns} =    copy.deepcopy    ${netset_conns_with_extra_mgmt_nw}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${sp_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${sp_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57546_sp['name']}

OVTC57547
    [Documentation]    Modify multiNIC netset SP and delete an existing connection
    [Tags]    TC35    SP    NET-SET
    [Setup]    Create SP with multi-NIC management OSDP    ${OVTC57547_sp}

    ${sp_dto} =    Get Resource  SP:${OVTC57547_sp['name']}
    Remove From Dictionary    ${sp_dto}    created    modified    status    state    status_code    headers
    ${new_conns} =    Delete Connection By Name    ${sp_dto['connectionSettings']['connections']}    ${new_mgmt_conn[0]['name']}
    Set To Dictionary    ${sp_dto['connectionSettings']}    connections=${new_conns}

    ${resp} =    Fusion Api Edit Server Profile    body=${sp_dto}    uri=${sp_dto['uri']}
    Wait For Task2    ${resp}    timeout=600    interval=5
    [Teardown]    Remove SP By Name    ${OVTC57547_sp['name']}

OVTC57549
    [Documentation]    Create SP from SPT using multi-NIC management OSDP with netset
    [Tags]    TC37    SP    NET-SET

    ${spt} =    copy.deepcopy    ${OVTC57549_spt}
    ${sp} =    copy.deepcopy    ${sp_from_spt}

    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Should Be True    ${blnCreateSPT}    Failed to create SPT: '${spt['name']}'

    ${blnCreateSPFromSPT} =    Create I3S SP from I3S SPT    ${sp}
    Should Be True    ${blnCreateSPFromSPT}    Failed to create profile '${sp['name']}'

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57549_spt['name']}

OVTC57550
    [Documentation]    Modify multiNIC netset SPT(which has SP created) and
    ...    choose different network from the netset in the OS deployment Setting
    [Tags]    TC38    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57550_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57550_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${osds} =    copy.deepcopy    ${spt_osds_with_diff_nws_of_netset}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57550_spt['name']}

OVTC57551
    [Documentation]    Modify multiNIC netset SPT(which has SP created)
    ...    and modify the netset connections to use different netset
    [Tags]    TC39    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57551_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57551_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${conns} =    copy.deepcopy    ${spt_change_netset_in_mgmt_conns['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${spt_osds_with_changed_mgmt_netset_conn}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'NonCompliant'
    ...    Fail    Profile is Compliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${sp_from_spt['name']}
    Should Be True    ${blnUpdateSp}    Failed to Update SP From SPT

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57551_spt['name']}

OVTC57552
    [Documentation]    Modify multiNIC netset SPT(which has SP created)
    ...    and rename the connections using netset
    [Tags]    TC40    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57552_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57552_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${conns} =    copy.deepcopy    ${netset_conns_with_diff_mgmt_nw_names}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57552_spt['name']}

OVTC57553
    [Documentation]    Modify multiNIC netset SPT(which has SP created) and replace netset with single networks
    [Tags]    TC41    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57553_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57553_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${conns} =    copy.deepcopy    ${spt_conn_settings['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${spt_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'NonCompliant'
    ...    Fail    Profile is Compliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${sp_from_spt['name']}
    Should Be True    ${blnUpdateSp}    Failed to Update SP From SPT

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57553_spt['name']}

OVTC57554
    [Documentation]    Modify multiNIC netset SPT(which has SP created)
    ...    and replace single network connection with Netset
    [Tags]    TC42    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57554_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57554_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${conns} =    copy.deepcopy    ${spt_conn_settings_with_netset['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}

    ${osds} =    copy.deepcopy    ${spt_osds}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'NonCompliant'
    ...    Fail    Profile is Compliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${sp_from_spt['name']}
    Should Be True    ${blnUpdateSp}    Failed to Update SP From SPT

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57554_spt['name']}

OVTC57555
    [Documentation]    Modify multiNIC netset SPT(which has SP created) and Add new connection
    [Tags]    TC43    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57555_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57555_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${conns} =    copy.deepcopy    ${netset_conns_with_extra_mgmt_nw}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57555_spt['name']}

OVTC57557
    [Documentation]    Modify multiNIC netset SPT(which has SP created) and delete an existing connection
    [Tags]    TC44    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57557_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57557_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${new_conns} =    Delete Connection By Name    ${spt_dto['connectionSettings']['connections']}    ${new_mgmt_conn[0]['name']}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${new_conns}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57557_spt['name']}

OVTC57559
    [Documentation]    Modify multiNIC netset SPT(which has SP created)
    ...    and modify existing single nic connection network with different network
    [Tags]    TC45    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57559_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57559_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    ${conns} =    copy.deepcopy    ${spt_conns_with_extra1_mgmt_conn['connections']}
    ${connections} =    Lookup connection uris    ${conns}
    Set To Dictionary    ${spt_dto['connectionSettings']}    connections=${connections}
    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'NonCompliant'
    ...    Fail    Profile is Compliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${sp_from_spt['name']}
    Should Be True    ${blnUpdateSp}    Failed to Update SP From SPT

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57559_spt['name']}

OVTC57560
    [Documentation]    Add a new network to netset and Modify multiNIC netset SPT(which has SP created) to use this network
    [Tags]    TC46    SPT    NET-SET
    [Setup]    Create SP from SPT with multi-NIC management OSDP    ${OVTC57560_spt}    ${sp_from_spt}

    ${spt_dto} =    Get Resource  SPT:${OVTC57560_spt['name']}
    Remove From Dictionary    ${spt_dto}    created    modified    status    state    status_code    headers

    Update Network Set    ${update_network_set}

    ${osds} =    copy.deepcopy    ${spt_ntive_osds_with_nws_from_diff_netset}
    ${osds_conns} =    Set OS Deployment settings    ${osds}
    Set To Dictionary    ${spt_dto}    osDeploymentSettings=${osds_conns}

    ${resp} =    Fusion Api Edit Server Profile Template    body=${spt_dto}    uri=${spt_dto['uri']}
    Wait For Task2    ${resp}    timeout=60    interval=5

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'NonCompliant'
    ...    Fail    Profile is Compliant after updating its SPT

    ${blnUpdateSp} =    Update SP From SPT    ${sp_from_spt['name']}
    Should Be True    ${blnUpdateSp}    Failed to Update SP From SPT

    # Verfying profile compliance with SPT
    ${sp_resp_after_updating_spt} =    Get Server Profile    ${sp_from_spt['name']}
    Should Be Equal As Strings    '${sp_resp_after_updating_spt['templateCompliance']}'    'Compliant'
    ...    Fail    Profile is NonCompliant after updating its SPT

    [Teardown]    Run Keywords
    ...    Update Network Set    ${revert_network_set}    AND
    ...    Remove SP By Name    ${sp_from_spt['name']}    AND
    ...    Remove SPT By Name    ${OVTC57560_spt['name']}

OVTC57563
    [Documentation]    Create SP and SPT using MultiNIC OSDP and provide no networks for NICs
    [Tags]    TC47    SP

    ${spt} =    copy.deepcopy    ${OVTC57563_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Should Not Be True    ${blnCreateSPT}    SPT: '${spt['name']}' created successfully which is not expected

    ${sp} =    copy.deepcopy    ${OVTC57563_sp}
    ${blnCreateSP} =    Create I3S Server Profile    ${sp}
    Should Not Be True    ${blnCreateSP}    SP: '${sp['name']}' created successfully which is not expected

    Run Keyword Unless    ${blnCreateSPT}==False and ${blnCreateSP}==False    Run Keywords
    ...    Should Not Be True    ${blnCreateSPT}    SPT '${spt['name']}' created successfully    AND
    ...    Should Not Be True    ${blnCreateSP}    SP '${sp['name']}' created successfully

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp['name']}    AND
    ...    Remove SPT By Name    ${spt['name']}

OVTC57565
    [Documentation]    Create SP and SPT using MultiNIC netset
    ...    and configure different networks from same netset for multiNICs
    [Tags]    TC48    SP    SPT    NET-SET

    ${spt} =    copy.deepcopy    ${OVTC57565_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}

    ${sp} =    copy.deepcopy    ${OVTC57565_sp}
    ${blnCreateSP} =    Create I3S Server Profile    ${sp}

    Run Keyword Unless    ${blnCreateSPT}==False and ${blnCreateSP}==False    Run Keywords
    ...    Should Not Be True    ${blnCreateSPT}    SPT '${spt['name']}' created successfully    AND
    ...    Should Not Be True    ${blnCreateSP}    SP '${sp['name']}' created successfully

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp['name']}    AND
    ...    Remove SPT By Name    ${spt['name']}

OVTC57567
    [Documentation]    Create SP and SPT using MultiNIC netset
    ...    and configure different networks from different netsets for multiNICs
    [Tags]    TC49    SP    SPT    NET-SET

    ${spt} =    copy.deepcopy    ${OVTC57567_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}
    Should Not Be True    ${blnCreateSPT}    SPT: '${spt['name']}' created successfully which is not expected

    ${sp} =    copy.deepcopy    ${OVTC57567_sp}
    ${blnCreateSP} =    Create I3S Server Profile    ${sp}
    Should Not Be True    ${blnCreateSP}    SP: '${sp['name']}' created successfully which is not expected

OVTC57569
    [Documentation]    Create SP and SPT using MultiNIC OSDP and configure one NIC with single network and another with netset network
    [Tags]    TC50    SP    SPT    NET-SET

    ${spt} =    copy.deepcopy    ${OVTC57569_spt}
    ${blnCreateSPT} =    Create I3S SPT    ${spt}

    ${sp} =    copy.deepcopy    ${OVTC57569_sp}
    ${blnCreateSP} =    Create I3S Server Profile    ${sp}

    Run Keyword Unless    ${blnCreateSPT}==False and ${blnCreateSP}==False    Run Keywords
    ...    Should Not Be True    ${blnCreateSPT}    SPT '${spt['name']}' created successfully    AND
    ...    Should Not Be True    ${blnCreateSP}    SP '${sp['name']}' created successfully

    [Teardown]    Run Keywords
    ...    Remove SP By Name    ${sp['name']}    AND
    ...    Remove SPT By Name    ${spt['name']}

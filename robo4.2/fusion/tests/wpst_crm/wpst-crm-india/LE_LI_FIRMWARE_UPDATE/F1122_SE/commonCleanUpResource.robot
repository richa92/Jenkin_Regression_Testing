*** Settings ***
Library    FusionLibrary


*** Variables ***
${APPLIANCE_IP}    ${EMPTY}


*** Keywords ***

Suite Clean Up Using FusionLibrary Resource
    [Documentation]    cleaning all components for other suite execution

    Log to console    \n****************************Clean Up*********************************
    Set Log Level    TRACE

    Log To Console    \n################### Login to appliance
    ${admin_credentials}    Create Dictionary    userName=Administrator    password=hpvse123
    Fusion Api Login Appliance     ${APPLIANCE_IP}   ${admin_credentials}

    Log To Console    \n################### Power off all servers
    Run Keyword and Ignore Error    server_hardware.Power off ALL servers

    Log To Console    \n################### Remove all SP's
    Run Keyword and Ignore Error    server_profile.Remove All Server Profiles

    Log To Console    \n################### Remove all LE's
    Run Keyword and Ignore Error    logical_enclosure.Remove All LEs

    Log To Console    \n################### Remove all EG's
    Run Keyword and Ignore Error    enclosure_group.Remove All Enclosure Groups

    Log To Console    \n################### Remove all LIG's
    Run Keyword and Ignore Error    logical_interconnect_group.Remove All LIGs

    Log To Console    \n################### Remove all FC Networks
    Run Keyword and Ignore Error    fc_network.Remove All FC Networks Async

    Log To Console    \n################### Remove all FCoE Networks
    Run Keyword and Ignore Error    fcoe_network.Remove All FCoE Networks

    Log To Console    \n################### Remove all Ethernet Networks
    Run Keyword and Ignore Error    ethernet_network.Remove All Ethernet Networks Async

    Log To Console    \n################### Remove all Stoage Volumes
    Run Keyword and Ignore Error    storage_volume.Remove ALL Storage Volumes Async    ?suppressDeviceUpdates=true

    Log To Console    \n################### Remove all Storage Systems
    Run Keyword and Ignore Error    storage_system.Remove ALL Storage Systems Async

    Log To Console    \n################### Remove all Users
    Run Keyword and Ignore Error    user.Remove All Users

    Log To Console    \n################### Logout appliance
    Fusion Api Logout Appliance
    Log to console    \n****************************Clean Up*********************************


Suite Clean Up Using Tests Resource
    [Documentation]    cleaning all components for other suite execution

    Log to console    \n****************************Clean Up*********************************

    Set Log Level    TRACE

    Log To Console    \n################### Login to appliance
    ${admin_credentials}    Create Dictionary    userName=Administrator    password=hpvse123
    Fusion Api Login Appliance     ${APPLIANCE_IP}   ${admin_credentials}

    Log To Console    \n################### Power off all servers
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Power off ALL servers

    Log To Console    \n################### Remove all SP's
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove All Server Profiles

    Log To Console    \n################### Remove all LE's
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove ALL Logical Enclosures

    Log To Console    \n################### Remove all EG's
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove ALL Enclosure Groups

    Log To Console    \n################### Remove all LIG's
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove ALL LIGs

    Log To Console    \n################### Remove all FC Networks
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove ALL FC Networks

    Log To Console    \n################### Remove all FCoE Networks
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove ALL FCoE Networks

    Log To Console    \n################### Remove all Ethernet Networks
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove ALL Ethernet Networks

    Log To Console    \n################### Remove all Users
    Run Keyword and Ignore Error    fusion_api_appliance_teardown.Remove ALL Users

    Log To Console    \n################### Logout appliance
    Fusion Api Logout Appliance
    Log to console    \n****************************Clean Up*********************************


Suite Clean Up Using wpst-crm Resource
    [Documentation]    cleaning all components for other suite execution

    Log to console    \n****************************Clean Up*********************************

    Set Log Level    TRACE

    Log To Console    \n################### Login to appliance
    ${admin_credentials}    Create Dictionary    userName=Administrator    password=hpvse123
    Fusion Api Login Appliance     ${APPLIANCE_IP}   ${admin_credentials}

    Log To Console    \n################### Remove all Users
    Run Keyword and Ignore Error    resource.Remove ALL Users

    Log To Console    \n################### Logout appliance
    Fusion Api Logout Appliance
    Log to console    \n****************************Clean Up*********************************


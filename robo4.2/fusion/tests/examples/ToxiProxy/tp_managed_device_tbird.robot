*** Settings ***
Documentation		Example test suite for using ToxiProxy to introduce increasing latency between OneView
...                 and "managed devices", i.e. a Blade iLO.  This demonstrates:
...                 1. ToxiProxy provisioning (installation, iptables, etc)
...                 2. Proxy creation
...                 3. Toxic creation and modification

Library    json
Library    FusionLibrary
Library    RoboGalaxyLibrary
Resource            /f420/fusion/Resources/api/fusion_api_resource.txt
Suite Setup         Suite Setup
Suite Teardown      Suite Teardown
Test Setup          Test Setup
Test Teardown       Test Teardown
*** Variables ***
${SKIPSETUP}                    ${False}
${SKIPTEARDOWN}                 ${False}
${VERBOSE}                      ${False}
${IP}             15.245.131.121             # appliance IP
${OV_IP}          fe80::b792:7d0e:5d91:a5e4  # OV primary mgmt ipv6
${TP}             fe80::9eb6:54ff:fe98:e068  # Dedicated IP for ToxiProxy managed device testing
${TPWPORT}        17988                      # ToxiProxy Webserver port - 8474 isn't allowed in PA!
${TPCIDR}         64                         # cidr for the Dedicated IP
${DEVICE_IP}      fe80::9af2:b3ff:fe22:48f0  # Managed device iLO IP, Bay 1 of WPST-PABA58-EN1, bay 2
${DEVICE_PORT}    6001                       # dedicated tcp port for the proxy traffic
${BLADE}          MXQ71906M9, bay 1
${PXY_NAME} =     ${DEVICE_PORT}proxy
${TX_NAME} =      ${DEVICE_PORT}latency_toxic
*** Test Cases ***
Refresh server without any toxics
    [Documentation]    This is just a control test case to show the refresh time without any proxy\toxics in place
    [Tags]   1
    ${task} =    Refresh server hardware    SH:${BLADE}
    ${resp} =    Wait for task2   ${task}    timeout=600   interval=15

Refresh Server with increasing latency
    [Documentation]    This test case will create a proxy and latency toxic, and then iterate a range of latency
    ...                values, increasing the latency each iteration and then performing a server refresh.
    [Tags]   2
    [Setup]      Proxy setup   proxy=${PXY_NAME}

    ${resp} =    Toxiproxy create a new toxic   proxy=${PXY_NAME}
    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"latency":50,"jitter":1}}

    :FOR    ${latency}   IN RANGE    50   201   50
    \    ${resp} =    Toxiproxy update an active toxic   proxy=${PXY_NAME}    toxic=${TX_NAME}
    \    ...   data={"name": "${TX_NAME}","type":"latency","stream":"upstream","attributes":{"latency":${latency},"jitter":1}}
    \    ${task} =    Refresh server hardware    SH:${BLADE}
    \    ${resp} =    Wait for task2   ${task}    timeout=600   interval=15

Remove toxic and refresh server
    [Documentation]    This test case demonstrates that removing the toxic brings normal operation back to refresh
    [Tags]   3
    ${resp} =    ToxiProxy Remove an active toxic    ${PXY_NAME}   ${TX_NAME}
    ${task} =    Refresh server hardware    SH:${BLADE}
    ${resp} =    Wait for task2   ${task}    timeout=600   interval=15

*** Keywords ***
Suite Setup
    [Documentation]   suite setup
    Return from keyword if   ${SKIPSETUP} is ${True}
    ToxiProxy install on appliance    ${IP}

Suite Teardown
    [Documentation]   suite teardown
    Return from keyword if   ${SKIPTEARDOWN} is ${True}
    ToxiProxy stop webserver on appliance    ${IP}
    ToxiProxy remove iptables files on appliance    ${IP}

Test Setup
    [Documentation]   test setup for all test cases
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance        ${IP}    ${admin_credentials}
    ${resp} =    Toxiproxy connect    ${IP}    ${TPWPORT}

Test Teardown
    [Documentation]   test teardown for all test cases
    Fusion Api Logout appliance

Proxy setup
    [Documentation]   steps to setup and create a proxy
    [Arguments]    ${proxy}
    Test Setup
    ToxiProxy add iptable file for managed device testing    ${IP}   ${OV_IP}  ${DEVICE_IP}   ${TP}   ${DEVICE_PORT}
    Start toxiproxy webserver
    ${pxy} =     ToxiProxy build proxy json    name=${proxy}
    ...                                        listen=[${TP}%bond0]:${DEVICE_PORT}
    ...                                        upstream=[${DEVICE_IP}]:443
    #...                                        transport=tcp
    ${resp} =    ToxiProxy Create a new proxy    ${pxy}

Start ToxiProxy Webserver
    [Documentation]   starts the webserver and verifies REST interaction by retrieving the TP version
    ${resp} =    ToxiProxy start webserver on appliance and open firewall port    ${IP}    ${TPWPORT}
    ${resp} =    Toxiproxy connect    ${IP}    ${TPWPORT}
    ${resp} =    Toxiproxy get version
    log   \n${resp}   console=True

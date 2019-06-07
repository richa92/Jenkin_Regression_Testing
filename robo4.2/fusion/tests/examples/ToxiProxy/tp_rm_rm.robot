*** Settings ***
Documentation		Example test suite for using ToxiProxy to introduce increasing latency between OneView
...                 and an RM.  This demonstrates:
...                 1. ToxiProxy provisioning (installation, iptables, listen.conf, etc)
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
${SKIPSETUP}      ${False}
${SKIPTEARDOWN}   ${False}
${VERBOSE}        ${False}
${IP}             15.245.132.42     # appliance IP
${TPWPORT}        17988             # ToxiProxy Webserver port - 8474 isn't allowed in PA!
${RMRMPORT}       8080              # new TCP port for RM-RM traffic
${BLADE}          WPST-PABA58-EN1, bay 2
${PXY_NAME} =     RM-RM-proxy
${TX_URL} =       server-hardware   # this is used by the custom latency toxic to filter RM requests
${TX_TYPE} =      http_latency      # this is the name of the custom latency toxic
${TX_NAME} =      ${TX_URL}_${TX_TYPE}_toxic

*** Test Cases ***
Refresh server without any toxins
    [Documentation]    This is just a control test case to show the refresh time without any proxy\toxics in place
    ${task} =    Refresh server hardware    SH:${BLADE}
    ${resp} =    Wait for task2   ${task}    timeout=600   interval=15

Refresh Server with increasing toxic latency for server-hardware uris
    [Documentation]    This test case will create a proxy and custom latency toxic, and then iterate a range of latency
    ...                values, increasing the latency each iteration and then performing a server refresh.

    [Setup]      Proxy setup   proxy=${PXY_NAME}

    ${resp} =    Toxiproxy create a new toxic   proxy=${PXY_NAME}
    ...   data={"name": "${TX_NAME}","type":"${TX_TYPE}","stream":"upstream","attributes":{"logfilename":"${TX_NAME}.log","urlsubstr":"${TX_URL}","latency":0,"jitter":1}}

    :FOR    ${latency}   IN RANGE    1000   4001   1000
    \    ${resp} =    Toxiproxy update an active toxic   proxy=${PXY_NAME}    toxic=${TX_NAME}
    \    ...   data={"name": "${TX_NAME}","type":"${TX_TYPE}","stream":"upstream","attributes":{"logfilename":"${TX_NAME}.log","urlsubstr":"${TX_URL}","latency":${latency},"jitter":1}}
    \    ${task} =    Refresh server hardware    SH:${BLADE}
    \    ${resp} =    Wait for task2   ${task}    timeout=1800   interval=15

Remove toxic and refresh server
    [Documentation]    This test case demonstrates that removing the toxic brings normal operation back to refresh
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
    ToxiProxy update listen.conf on appliance for RM to RM testing    ${IP}   80

Test Setup
    [Documentation]   test setup for all test cases
	${admin_credentials} =      json.loads    {"userName": "Administrator", "password": "hpvse123"}
    Fusion Api Login Appliance        ${IP}    ${admin_credentials}

Test Teardown
    [Documentation]   test teardown for all test cases
    Fusion Api Logout appliance

Proxy setup
    [Documentation]   steps to setup and create a proxy
    [Arguments]    ${proxy}
    Test Setup
    # update listen.conf
    ${resp} =    ToxiProxy update listen.conf on appliance for RM to RM testing    ${IP}   ${RMRMPORT}
    Start toxiproxy webserver
    ${resp} =    Toxiproxy connect    ${IP}    ${TPWPORT}
    ${pxy} =     ToxiProxy build proxy json    name=${proxy}
    ...                                        listen=0.0.0.0:80
    ...                                        upstream=0.0.0.0:${RMRMPORT}
    ${resp} =    ToxiProxy Create a new proxy    ${pxy}
    Log   ${proxy} created successfully    console=True

Start ToxiProxy Webserver
    [Documentation]   starts the webserver and verifies REST interaction by retrieving the TP version
    ${resp} =    ToxiProxy start webserver on appliance and open firewall port    ${IP}    ${TPWPORT}
    ${resp} =    Toxiproxy connect    ${IP}    ${TPWPORT}
    ${resp} =    Toxiproxy get version
    log   \n${resp}   console=True

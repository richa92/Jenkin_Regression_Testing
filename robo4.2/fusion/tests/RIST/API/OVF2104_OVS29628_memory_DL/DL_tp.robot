*** Settings ***
Library    RoboGalaxyLibrary
Library    json

Suite Setup     Install ToxiProxy
Test Setup      Test Setup

*** Variables ***
${SKIPSETUP}                    ${False}
${IP}           16.114.219.74    # appliance IP
${TPPORT}       17988
${TP}           16.114.213.34    # Dedicated IP for ToxiProxy managed device testing
${DEVICE_IP}    16.114.212.92     # Managed device iLO IP

*** Test Cases ***
#Add an interface to the appliance
#    ${resp} =     ToxiProxy add IP to appliance for managed device testing    ${IP}    ${TP}   20
#    log   \n${resp}   console=True

#Update listen.conf for RM to RM testing
#    ${resp} =     ToxiProxy update listen.conf on appliance for RM to RM testing    ${IP}    8080
#    log   \n${resp}   console=True

Add iptables entry for managed device testing
    ${resp} =     ToxiProxy add iptable file for managed device testing    ${IP}   ${DEVICE_IP}   ${TP}    6001
    log   \n${resp}   console=True

Create a proxy
    ${resp} =    ToxiProxy Create a new proxy   {"name":"http_proxy3","listen":"${TP}:6001","upstream":"${DEVICE_IP}:443","enabled":true,"toxics":[]}
    log   \n${resp} ${resp.content}  console=True

Create a toxic
#    /root/rpm/toxiproxy-cli-linux-amd64 toxic add http_proxy -n latency_up -t latency --upstream  -a latency=3000
    ${resp} =    Toxiproxy create a new toxic   http_proxy3   {"name": "toxic1","type":"latency","stream":"upstream","attributes":{"latency":3000,"jitter":1}}
    log   \n${resp} ${resp.content}  console=True

List proxies and toxics
    ${resp} =    ToxiProxy List existing proxies and their toxics
    log   \n${resp}   console=True

#Update a toxic
#    ${resp} =    Toxiproxy update an active toxic   http_proxy3    toxic1   {"name": "toxic1","type":"latency","stream":"downstream","toxicity":2.0,"attributes":{"latency":2,"jitter":2}}
#    log   \n${resp} ${resp.content}  console=True
#    ${resp} =    ToxiProxy List existing proxies and their toxics
#    log   \n${resp}   console=True

#Enable all proxies, remove toxics
#    ${resp} =    ToxiProxy Enable all proxies and remove all active toxics    ${None}
#    log   \n${resp} ${resp.content}  console=True

Stop toxiproxy
    ${resp} =    ToxiProxy stop webserver on appliance    ${IP}
    log   \n${resp}   console=True

Revert iptables
    ${resp} =    ToxiProxy remove iptables files on appliance    ${IP}
    log   \n${resp}   console=True
    should not contain    ${resp}    failed

*** Keywords ***
Test Setup
    [Documentation]  Setup
    ${resp} =    Toxiproxy connect    ${IP}    ${TPPORT}

Install ToxiProxy
    [Documentation]  Install ToxiProxy
    Return from keyword if   ${SKIPSETUP} is ${True}
    ${resp} =    ToxiProxy install on appliance    ${IP}
    ${resp} =    ToxiProxy start webserver on appliance and open firewall port    ${IP}    ${TPPORT}
    ${resp} =    Toxiproxy connect    ${IP}    ${TPPORT}
    ${resp} =    Toxiproxy get version
    log   \n${resp}   console=True

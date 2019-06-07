*** Settings ***
Documentation    Run First Time Setup on newly deployed DCS VM
Resource         resource.txt

*** Test Cases ***
First Time Setup
    [Tags]    FTS
    [Documentation]     Configure First time setup for OneView Appliance
    Update Appliance Data
    First Time Setup  ${DATA}  ${ADMIN_CREDENTIALS['password']}
    Wait For Appliance To Become Pingable  ${APPLIANCE_IP}

*** Keywords ***
Update Appliance Data
    [Documentation]    New appliance IP, iptype and hostname will be updated at run time
    ${list}=  Collections.Get From Dictionary    ${APPLIANCE}    applianceNetworks
    ${net}=  Collections.Get From List    ${list}    0
    Log to console and logfile          update applinace VIRTIPV4ADDR is : ${VIRTIPV4ADDR}
	Log to console and logfile          update appliance APP1IPV4ADDR is : ${APP1IPV4ADDR}
    Collections.Remove From Dictionary    ${net}    virtIpv4Addr    ipv4Type    hostname     app1Ipv4Addr
    Run Keyword If   '${APP1IPV4ADDR}' is not 'None'    Collections.Set To Dictionary   ${net}   ipv4Type=${IPV4TYPE}    app1Ipv4Addr=${APP1IPV4ADDR}    hostname=${HOSTNAME}
	...             ELSE IF     '${virtIpv4Addr}' is not 'None'  Collections.Set To Dictionary   ${net}   ipv4Type=${IPV4TYPE}    virtIpv4Addr=${VIRTIPV4ADDR}    hostname=${HOSTNAME}
	...             ELSE    Log     Either app1Ipv4Addr or virtIpv4Addr must be provided in the 'appliance' variable in your data file     WARN
    ${network_list}=    Create List    ${net}
    Log to console and logfile         ${net}
    Collections.Remove From Dictionary    ${APPLIANCE}    applianceNetworks
    Collections.Set To Dictionary    ${APPLIANCE}    applianceNetworks=${network_list}
    Log to console and logfile       ${APPLIANCE}

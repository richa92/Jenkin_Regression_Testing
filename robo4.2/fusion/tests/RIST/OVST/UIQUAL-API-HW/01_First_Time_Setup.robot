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
    Collections.Remove From Dictionary    ${net}    virtIpv4Addr    ipv4Type    hostname
    Collections.Set To Dictionary   ${net}   virtIpv4Addr=${VIRTIPV4ADDR}    ipv4Type=${IPV4TYPE}
    ...    hostname=${HOSTNAME}
    ${network_list}=    Create List    ${net}
    Collections.Remove From Dictionary    ${APPLIANCE}    applianceNetworks
    Collections.Set To Dictionary    ${APPLIANCE}    applianceNetworks=${network_list}

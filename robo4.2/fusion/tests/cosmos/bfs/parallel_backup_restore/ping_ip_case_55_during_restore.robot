*** Settings ***
Documentation    Backup and Restore of OV appliance
Resource                        ../resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test cases ***
IP Should Be Pinging During Oneview Restore
     [Tags]  ENC126  CASE55
     [Documentation]     IP Should Be Pinging During Oneview Restore
     Sleep     2sec  #Wait for Backup process to begin
     Wait Until Keyword Succeeds  ${timeout}    ${interval}   Get Backup status and wait till completed
     ${profilename}=     Get From Dictionary  ${iscsi_case55_profile[0]}  name
     ${win_ip}=    create list
     ${profiles} =       Fusion Api Get Server Profiles  param=?count=10&filter="name matches '%25${profilename}%25'"
     ${resp} =      Get Server Ethernet Connections IPs from DHCP  @{profiles['members']}
     ${count} =      Get Length      ${resp}
     Run Keyword if      ${count} == 0     FAIL    No IP's found in DHCP server
     :FOR   ${ips}    IN   @{resp}
     \      ${status}     ${response}=     Run Keyword and Ignore Error      Ping IPAddress    ${ips}
     \      ${ip}=     Convert To String   ${ips}
     \      Run Keyword If      '${status}'=='PASS'     Append to list  ${win_ip}   ${ip}
     ${count} =      Get Length      ${win_ip}
     Run Keyword if      ${count} == 0     FAIL    No IP's are pingable
     Wait Until Keyword Succeeds     ${timeout}   ${interval}   Connectivity Validation until appliance restore is completed  ${win_ip[0]}


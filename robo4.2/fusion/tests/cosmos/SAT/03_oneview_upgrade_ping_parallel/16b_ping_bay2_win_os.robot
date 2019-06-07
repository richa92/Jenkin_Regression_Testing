*** Settings ***
Documentation
...     Ping IP during backup and restore
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup    ${ad_server_credentials}

*** Variables ***
${fail} =    ${0}
${count} =    ${500}
${failure_count} =    ${3}
${tbird_count} =    ${700}

*** Test cases ***
IP Should Be Pinging During Oneview Restore-Bay2 - C7000
     [Tags]      PING   C7000
     [Documentation]     IP Should Be Pinging During Oneview Restore
     @{ips}=    create list
     :FOR  ${win_os_server}  IN   @{win_os_servers}
     \     ${resp} =      Get IP From Server Profile   ${win_os_server}
     \     append to list   ${ips}    ${resp}
     :For  ${ip}  IN  @{ips[1]}
     \    Set Variable  ${ip}
     :FOR  ${index}  IN RANGE  ${count}
     \  ${passed}=  Run Keyword and Return Status   Ping IPAddress  ${ip}
     \  Continue For Loop If  ${passed}
     \  ${fail}=  Evaluate      ${fail} + 1
     ${success}=  Evaluate      ${count} - ${fail}
     Log Many   Success:  ${success}   console=True
     Log Many   fail:  ${fail}   console=True
     Run keyword if  ${fail} > ${failure_count}    FAIL   Ping failure count is more than ${failure_count}

IP Should Be Pinging During Oneview Restore-Bay2 - Tbird
     [Tags]      PING  T-BIRD
     [Documentation]     IP Should Be Pinging During Oneview Restore
     @{ips}=    create list
     :FOR  ${win_os_server}  IN   @{win_os_servers}
     \     ${resp} =      Get IP From Server Profile   ${win_os_server}
     \     append to list   ${ips}    ${resp}
     :For  ${ip}  IN  @{ips[1]}
     \    Set Variable  ${ip}
     :FOR  ${index}  IN RANGE  ${tbird_count}
     \  ${passed}=  Run Keyword and Return Status   Ping IPAddress  ${ip}
     \  Continue For Loop If  ${passed}
     \  ${fail}=  Evaluate      ${fail} + 1
     ${success}=  Evaluate      ${tbird_count} - ${fail}
     Log Many   Success:  ${success}   console=True
     Log Many   fail:  ${fail}   console=True
     Run keyword if  ${fail} > ${failure_count}    FAIL   Ping failure count is more than ${failure_count}
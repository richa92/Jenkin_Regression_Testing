*** Settings ***
Documentation
...     Ping IP during appliance reboot
Resource                        ../resource.txt
Suite Setup             Regression Test Setup    ${ad_server_credentials}
Suite Teardown          Regression Test Teardown

*** Variables ***
${fail} =    ${0}
${count} =    ${500}
${failure_count} =    ${3}

*** Test cases ***
IP Should Be Pinging During Appliance Reboot-Bay1 - C7000
     [Tags]      PING  C7000   4.0   3.10
     [Documentation]     IP Should Be Pinging During appliance reboot
     @{ips}=    create list
     :FOR  ${win_os_server}  IN   @{win_os_servers}
     \     ${resp} =      Get IP From Server Profile   ${win_os_server}
     \     append to list   ${ips}    ${resp}
     :For  ${ip}  IN  @{ips[0]}
     \    Set Variable  ${ip}
     :FOR  ${index}  IN RANGE  ${count}
     \  ${passed}=  Run Keyword and Return Status   Ping IPAddress  ${ip}
     \  Continue For Loop If  ${passed}
     \  ${fail}=  Evaluate      ${fail} + 1
     ${success}=  Evaluate      ${count} - ${fail}
     Log Many   Success:  ${success}   console=True
     Log Many   fail:  ${fail}   console=True
     Run keyword if  ${fail} > ${failure_count}    FAIL   Ping failure count is more than ${failure_count}
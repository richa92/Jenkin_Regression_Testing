*** Settings ***
Documentation    Uplink failover in interconnect for ethernet and non-ethernet ports.
...     TAGS:                      CABLE-PULL
Resource                        ../resource.txt
Suite Setup                     Regression Test Setup     ${admin_credentials}
Suite Teardown                  Run Keywords    Run Keyword If Any Tests Failed  Get Support Dump  ${support_dump}  ${SUITE NAME}
...                             AND  Run Keyword If Any Tests Failed  Get LE Support Dump  ${le_support_dump_postexec}  ${SUITE NAME}
...                             AND  Regression Test Teardown

*** Test Cases ***
Simulate a failure in the IC Uplink port in interconnect for ethernet 1 port
   [Documentation]     Disable IC Uplink Port in interconnect for ethernet port
   [Tags]      ETH-UPLINK-FAIL  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect1_eth_disable}

Simulate a failure in the IC Uplink ports in interconnect for non-ethernet 1 port
   [Documentation]     Disable IC Uplink Port in interconnect for non-ethernet port
   [Tags]      NETH-UPLINK-FAIL  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect3_neth_disable}

Ping IP Post Disable Uplink, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST-UPLINK-FAIL  C7000
   [Documentation]     Ping IP Post Disabling Uplink, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   :FOR  ${win_os_server}  IN   @{win_os_servers}
   \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active    ${win_os_server}   01

Enable IC Uplink ports in interconnect for non-ethernet 1 port
   [Documentation]     Enable IC Uplink Port in interconnect for non-ethernet port
   [Tags]      NETH-UPLINK-EN  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect1_eth_enable}

Enable IC Uplink ports in interconnect for ethernet 1 port
   [Documentation]     Enable IC Uplink Port in interconnect for ethernet port
   [Tags]      ETH-UPLINK-EN  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect3_neth_enable}

Ping IP Post Enable Uplink, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST-UPLINK-EN  C7000
   [Documentation]     Ping IP Post Disabling Uplink, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   :FOR  ${win_os_server}  IN   @{win_os_servers}
   \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active    ${win_os_server}   02

Simulate a failure in the IC Uplink port in interconnect for ethernet 2 port
   [Documentation]     Disable IC Uplink Port in interconnect for ethernet port
   [Tags]      ETH-UPLINK-FAIL  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect2_eth_disable}

Simulate a failure in the IC Uplink ports in interconnect for non-ethernet 2 port
   [Documentation]     Disable IC Uplink Port in interconnect for non-ethernet port
   [Tags]      NETH-UPLINK-FAIL  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect4_neth_disable}

Ping IP Post Disable Uplink 2, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST-UPLINK-FAIL  C7000
   [Documentation]     Ping IP Post Disabling Uplink, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   :FOR  ${win_os_server}  IN   @{win_os_servers}
   \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active    ${win_os_server}   01

Enable IC Uplink ports in interconnect for non-ethernet 2 port
   [Documentation]     Enable IC Uplink Port in interconnect for non-ethernet port
   [Tags]      NETH-UPLINK-EN  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect2_eth_enable}

Enable IC Uplink ports in interconnect for ethernet 2 port
   [Documentation]     Enable IC Uplink Port in interconnect for ethernet port
   [Tags]      ETH-UPLINK-EN  C7000
   Simulate a failure in the IC Uplink ports  ${interconnect4_neth_enable}

Ping IP Post Enable Uplink 2, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   [Tags]      POST-UPLINK-EN  C7000
   [Documentation]     Ping IP Post Disabling Uplink, Windows Server Should Be Pinging, FCoE Disk Should Exist and Active
   :FOR  ${win_os_server}  IN   @{win_os_servers}
   \  Run Keyword And Continue On Failure   Windows Server Should Be Pinging And Volume Should Be Active    ${win_os_server}   02
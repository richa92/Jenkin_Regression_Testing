*** Settings ***
Documentation    Uplink failover in interconnect for ethernet and non ethernet ports
Resource                        resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test cases ***
Simulate a failure in the IC Uplink port in interconnect for ethernet and non ethernet port - A side
   [Documentation]     Disable IC Uplink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]      PRE-DIS-ASIDE
   Update IC Uplink Port and wait until port reaches desired state  ${interconnect_aside_disable}

Enable IC Uplink ports in interconnect for Ethernet and non-ethernet port - A side
   [Documentation]     Enable IC Uplink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]     PRE-EN-ASIDE
   Update IC Uplink Port and wait until port reaches desired state  ${interconnect_aside_enable}

Simulate a failure in the IC Uplink port in interconnect for ethernet and non ethernet port - B side
   [Documentation]     Disable IC Uplink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-DIS-BSIDE
   Update IC Uplink Port and wait until port reaches desired state  ${interconnect_bside_disable}

Enable IC Uplink ports in interconnect for Ethernet and non-ethernet port - B side
   [Documentation]     Enable IC Uplink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-EN-BSIDE
   Update IC Uplink Port and wait until port reaches desired state  ${interconnect_bside_enable}


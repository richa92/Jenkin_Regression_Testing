*** Settings ***
Documentation    Downlink failover in interconnect for ethernet and non ethernet ports
Resource                        resource.txt
Suite Setup                     BFS OV Suite Setup    ${admin_credentials}
Suite Teardown                  BFS OV Suite Teardown

*** Test cases ***
Simulate a failure in the IC Downlink port in interconnect for ethernet and non ethernet port - A side
   [Documentation]     Disable IC Downlink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]      PRE-DIS-ASIDE  Synergy
   Update IC Downlink Port and wait until port reaches desired state  ${interconnect_down_aside_disable}

Enable IC Downlink ports in interconnect for Ethernet and non-ethernet port - A side
   [Documentation]     Enable IC Downlink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]     PRE-EN-ASIDE  Synergy
   Update IC Downlink Port and wait until port reaches desired state  ${interconnect_down_aside_enable}

Simulate a failure in the IC Downlink port in interconnect for ethernet and non ethernet port - B side
   [Documentation]     Disable IC Downlink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-DIS-BSIDE  Synergy
   Update IC Downlink Port and wait until port reaches desired state  ${interconnect_down_bside_disable}

Enable IC Downlink ports in interconnect for Ethernet and non-ethernet port - B side
   [Documentation]     Enable IC Downlink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-EN-BSIDE  Synergy
   Update IC Downlink Port and wait until port reaches desired state  ${interconnect_down_bside_enable}

Simulate a failure in the IC Downlink port in interconnect for ethernet and non ethernet port - A side
   [Documentation]     Disable IC Downlink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]      PRE-DIS-ASIDE1  C7K  Run1
   Update IC Downlink Port and wait until port reaches desired state  ${run1_interconnect_down_aside_disable}

Enable IC Downlink ports in interconnect for Ethernet and non-ethernet port - A side
   [Documentation]     Enable IC Downlink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]     PRE-EN-ASIDE1  C7K  Run1
   Update IC Downlink Port and wait until port reaches desired state  ${run1_interconnect_down_aside_enable}

Simulate a failure in the IC Downlink port in interconnect for ethernet and non ethernet port - B side
   [Documentation]     Disable IC Downlink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-DIS-BSIDE1  C7K  Run1
   Update IC Downlink Port and wait until port reaches desired state  ${run1_interconnect_down_bside_disable}

Enable IC Downlink ports in interconnect for Ethernet and non-ethernet port - B side
   [Documentation]     Enable IC Downlink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-EN-BSIDE1  C7K  Run1
   Update IC Downlink Port and wait until port reaches desired state  ${run1_interconnect_down_bside_enable}

Simulate a failure in the IC Downlink port in interconnect for ethernet and non ethernet port - A side
   [Documentation]     Disable IC Downlink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]      PRE-DIS-ASIDE2  C7K  Run2
   Update IC Downlink Port and wait until port reaches desired state  ${run2_interconnect_down_aside_disable}

Enable IC Downlink ports in interconnect for Ethernet and non-ethernet port - A side
   [Documentation]     Enable IC Downlink Port in interconnect for ethernet port and non ethernet port - A side
   [Tags]     PRE-EN-ASIDE2  C7K  Run2
   Update IC Downlink Port and wait until port reaches desired state  ${run2_interconnect_down_aside_enable}

Simulate a failure in the IC Downlink port in interconnect for ethernet and non ethernet port - B side
   [Documentation]     Disable IC Downlink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-DIS-BSIDE2  C7K  Run2
   Update IC Downlink Port and wait until port reaches desired state  ${run2_interconnect_down_bside_disable}

Enable IC Downlink ports in interconnect for Ethernet and non-ethernet port - B side
   [Documentation]     Enable IC Downlink Port in interconnect for ethernet port and non ethernet port - B side
   [Tags]      PRE-EN-BSIDE2  C7K  Run2
   Update IC Downlink Port and wait until port reaches desired state  ${run2_interconnect_down_bside_enable}